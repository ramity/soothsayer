import os

class EnvConfig:

    # python internal flask config - http://flask.pocoo.org/docs/1.0/config/#builtin-configuration-values

    FLASK_APP                                  = os.getenv("FLASK_APP", None)
    FLASK_ENV                                  = os.getenv("FLASK_ENV", "production")
    ENV                                        = os.getenv("ENV", True if FLASK_ENV == "development" else False)
    DEBUG                                      = os.getenv("DEBUG", True)
    TESTING                                    = os.getenv("TESTING", False)
    PROPAGATE_EXCEPTIONS                       = os.getenv("PROPAGATE_EXCEPTIONS", None)
    PRESERVE_CONTEXT_ON_EXCEPTION              = os.getenv("PRESERVE_CONTEXT_ON_EXCEPTION", None)
    TRAP_HTTP_EXCEPTIONS                       = os.getenv("TRAP_HTTP_EXCEPTIONS", False)
    TRAP_BAD_REQUEST_ERRORS                    = os.getenv("TRAP_BAD_REQUEST_ERRORS", None)
    SECRET_KEY                                 = os.getenv("SECRET_KEY", None)
    SESSION_COOKIE_NAME                        = os.getenv("SESSION_COOKIE_NAME", "session")
    SESSION_COOKIE_DOMAIN                      = os.getenv("SESSION_COOKIE_DOMAIN", None)
    SESSION_COOKIE_PATH                        = os.getenv("SESSION_COOKIE_PATH", None)
    SESSION_COOKIE_HTTPONLY                    = os.getenv("SESSION_COOKIE_HTTPONLY", True)
    SESSION_COOKIE_SECURE                      = os.getenv("SESSION_COOKIE_SECURE", False)
    SESSION_COOKIE_SAMESITE                    = os.getenv("SESSION_COOKIE_SAMESITE", None)
    PERMANENT_SESSION_LIFETIME                 = os.getenv("PERMANENT_SESSION_LIFETIME", "2678400")
    SESSION_REFRESH_EACH_REQUEST               = os.getenv("SESSION_REFRESH_EACH_REQUEST", True)
    USE_X_SENDFILE                             = os.getenv("USE_X_SENDFILE", False)
    SEND_FILE_MAX_AGE_DEFAULT                  = int(os.getenv("SEND_FILE_MAX_AGE_DEFAULT", 43200))
    SERVER_NAME                                = os.getenv("SERVER_NAME", None)
    APPLICATION_ROOT                           = os.getenv("APPLICATION_ROOT", "/")
    PREFERRED_URL_SCHEME                       = os.getenv("PREFERRED_URL_SCHEME", "http")
    MAX_CONTENT_LENGTH                         = os.getenv("MAX_CONTENT_LENGTH", None)
    JSON_AS_ASCII                              = os.getenv("JSON_AS_ASCII", True)
    JSON_SORT_KEYS                             = os.getenv("JSON_SORT_KEYS", True)
    JSONIFY_PRETTYPRINT_REGULAR                = os.getenv("JSONIFY_PRETTYPRINT_REGULAR", False)
    JSONIFY_MIMETYPE                           = os.getenv("JSONIFY_MIMETYPE", "application/json")
    TEMPLATES_AUTO_RELOAD                      = os.getenv("TEMPLATES_AUTO_RELOAD", None)
    EXPLAIN_TEMPLATE_LOADING                   = os.getenv("EXPLAIN_TEMPLATE_LOADING", False)
    MAX_COOKIE_SIZE                            = int(os.getenv("MAX_COOKIE_SIZE", 4093))

    # python internal mongo config - http://flask-pymongo.readthedocs.io/en/latest/#configuration

    MONGODB_SETTINGS                           = {}
    MONGODB_SETTINGS["db"]                     = os.getenv("MONGODB_DB", "knife")
    MONGODB_SETTINGS["host"]                   = os.getenv("MONGODB_HOST", "mongodb")
    MONGODB_SETTINGS["port"]                   = int(os.getenv("MONGODB_PORT", 27017))
    MONGODB_SETTINGS["username"]               = os.getenv("MONGODB_USERNAME", "root")
    MONGODB_SETTINGS["password"]               = os.getenv("MONGODB_PASSWORD", "foobar")
    MONGODB_SETTINGS["authentication_source"]  = os.getenv("MONGODB_AUTHENTICATION_SOURCE", "admin")
