from flask import Blueprint, render_template, request
from flask_login import current_user
from werkzeug.exceptions import NotFound
from flask_babel import gettext
import critiquebrainz.db.review as db_review
import critiquebrainz.frontend.external.musicbrainz_db.recording as mb_recording
import critiquebrainz.frontend.external.musicbrainz_db.exceptions as mb_exceptions
from critiquebrainz.frontend.forms.rate import RatingEditForm
from critiquebrainz.frontend.views import get_avg_rating, RECORDING_REVIEWS_LIMIT


recording_bp = Blueprint('recording', __name__)


@recording_bp.route('/<uuid:id>')
def entity(id):
    id = str(id)
    try:
        recording = mb_recording.get_recording_by_id(id)
    except mb_exceptions.NoDataFoundException:
        raise NotFound(gettext("Sorry, we couldn't find a recording with that MusicBrainz ID."))

    if 'url-rels' in recording:
        external_reviews = list(filter(lambda rel: rel['type'] == 'review', recording['url-rels']))
    else:
        external_reviews = []

    limit = int(request.args.get('limit', default=RECORDING_REVIEWS_LIMIT))
    offset = int(request.args.get('offset', default=0))
    if current_user.is_authenticated:
        my_reviews, my_count = db_review.list_reviews(
            entity_id=recording['id'],
            entity_type='recording',
            user_id=current_user.id,
        )
        my_review = my_reviews[0] if my_count else None
    else:
        my_review = None
    reviews, count = db_review.list_reviews(
        entity_id=recording['id'],
        entity_type='recording',
        sort='popularity',
        limit=limit,
        offset=offset,
    )
    avg_rating = get_avg_rating(recording['id'], "recording")

    rating_form = RatingEditForm(entity_id=id, entity_type='recording')
    rating_form.rating.data = my_review['rating'] if my_review else None

    return render_template('recording/entity.html', id=recording['id'], recording=recording, reviews=reviews,
                           my_review=my_review, external_reviews=external_reviews, limit=limit, offset=offset,
                           count=count, avg_rating=avg_rating, rating_form=rating_form, current_user=current_user)
