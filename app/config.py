import os

POSTGRES = {
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'pw': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'db': os.environ.get('POSTGRES_DB', 'appdb'),
    'host': os.environ.get('POSTGRES_HOST', 'db'),
    'port': os.environ.get('POSTGRES_PORT', '5432'),
}

SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES['user']}:{POSTGRES['pw']}@"
    f"{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False