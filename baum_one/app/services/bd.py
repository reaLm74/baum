from app.db.db import async_session_maker
from app.models.data import DataTable
from sqlalchemy import select


async def save_meta(name, size) -> None:
    async with async_session_maker() as session:
        create_product = DataTable(
            name=name,
            size=size
        )
        session.add(create_product)
        await session.commit()


async def get_metadata():
    async with async_session_maker() as session:
        query = select(DataTable)
        metadata = await session.scalars(query)
    return metadata
