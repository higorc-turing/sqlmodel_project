from sqlmodel import SQLModel


class DeveloperBase(SQLModel):
    name: str
    country: str

class DeveloperRead(DeveloperBase):
    pass
