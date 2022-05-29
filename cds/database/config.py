from sqlmodel import Session, create_engine

from cds.settings import ENV_VARS

DATABASE_URI = (
    f"mysql://{ENV_VARS.CDS_MYSQL_USER}:{ENV_VARS.CDS_MYSQL_PASSWORD.get_secret_value()}"
    f"@{ENV_VARS.CDS_MYSQL_SERVER}:{ENV_VARS.CDS_MYSQL_PORT.get_secret_value()}"
    f"/{ENV_VARS.CDS_MYSQL_DATABASE}"
)

engine = create_engine(
    DATABASE_URI,
    echo=True,
    # connect_args={'check_same_thread': False}
)

def session_maker():
    return Session(engine)
