def cache_config():
    config = {
        "DEBUG": True,  # some Flask specific configs
        "CACHE_TYPE": "simple",  # Flask-Caching related configs
        "CACHE_DEFAULT_TIMEOUT": 300
    }
    return config
