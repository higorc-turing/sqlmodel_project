from sqlmodel import Session, create_engine

sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    sqlite_url,
    echo=True,
    connect_args={
        'check_same_thread': False
    }
)

def get_session():
    return Session(engine)
