from app.db.db import Base
from sqlalchemy import Column, Integer, String


class DataTable(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
