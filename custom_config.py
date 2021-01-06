# CUSTOM CONFIGURATION FILE
# Optional variables are commented out.

DEBUG = True  # set to False in production mode

SECRET_KEY = "CHANGE_THIS"


# LOGGING

#LOG_FILE = {
#    "filename": "./logs/log.txt",
#    "max_bytes": 512 * 1024,  # optional
#    "backup_count": 100,      # optional
#}

#LOG_EMAIL = {
#    "mail_server": "localhost",
#    "mail_port": 25,
#    "mail_from_host": "example.org",
#    "log_email_recipients": [
#        "user1@example.org",
#        "user2@example.org",
#    ],
#    "log_email_topic": "CritiqueBrainz Failure",
#    "level": "ERROR",  # optional
#}

#LOG_SENTRY = {
#    "dsn": "YOUR_SENTRY_DSN",
#    "level": "WARNING",  # optional
#}


# EXTERNAL SERVICES

# MusicBrainz
#MUSICBRAINZ_HOSTNAME = "localhost:5000"
#MUSICBRAINZ_USERAGENT = "CritiqueBrainz Custom"
MUSICBRAINZ_CLIENT_ID = "cMkAG69nDmchFlYe0jnwkx6qIdhVwZWv"
MUSICBRAINZ_CLIENT_SECRET = "v4fCyqncJMmjehJCe64VqRtCvXi05cBG"

# Server with Spotify mappings
# https://github.com/metabrainz/mbspotify
#MBSPOTIFY_BASE_URI = "https://mbspotify.musicbrainz.org/"
#MBSPOTIFY_ACCESS_KEY = ""

# Spotify
#SPOTIFY_CLIENT_ID = ""
#SPOTIFY_CLIENT_SECRET = ""

# OTHER STUFF

# List of administrators (MusicBrainz usernames as strings)
ADMINS = []

# Mail server
#MAIL_SERVER = 'localhost'
#MAIL_PORT = 25
#MAIL_USERNAME = None
#MAIL_PASSWORD = None
#MAIL_FROM_ADDR = "no-reply@critiquebrainz.org"

#DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

#GOOGLE_ANALYTICS_TRACKING_ID = ""
