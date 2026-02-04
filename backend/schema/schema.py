LOG_COLUMNS = ["timestamp", "level", "service", "message"]

LOG_TYPES = {"timestamp":"datetime64[ns]",
             "level": "category",
             "service": "string",
             "message": "string"
            }

ANAMOLY_SCHEMA = ["timestamp", "error_count", "z_score", "is_anamoly"]