from sqlmodel import Session, create_engine

from cds.settings import ENV_VARS

DATABASE_URL = 'mysql://{user}:{password}@{address}:{port}/{database}'.format(
    user=ENV_VARS.CDS_MYSQL_USER,
    password=ENV_VARS.CDS_MYSQL_PASSWORD.get_secret_value(),
    address=ENV_VARS.CDS_MYSQL_ADDRESS.get_secret_value(),
    port=ENV_VARS.CDS_MYSQL_PORT.get_secret_value(),
    database=ENV_VARS.CDS_MYSQL_DATABASE
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    # connect_args={'check_same_thread': False}
)

def session_maker():
    return Session(engine)
