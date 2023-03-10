
import os


class OpenCDMSConfig:
    CDM_DB_HOST = os.getenv("CDM_DB_HOST", "127.0.0.1")
    CDM_DB_PORT = os.getenv("CDM_DB_PORT", 5432)
    CDM_DB_USER = os.getenv("CDM_DB_USER", "postgres")
    CDM_DB_PASS = os.getenv("CDM_DB_PASSWORD", "password")
    CDM_DB_NAME = os.getenv("CDM_DB_NAME", "postgres")
    CDM_DB_ENGINE = os.getenv("CDM_DB_ENGINE", "postgresql")
    CDM_DB_DRIVER = os.getenv("CDM_DB_DRIVER", "psycopg2")
config = OpenCDMSConfig()
