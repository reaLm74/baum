import asyncio

from app.services.bd import save_meta
from app.services.data import comparison_result
from app.services.file import save_file


async def consume_file_meta_save(consumer):
    try:
        async for msg in consumer:
            value = eval(msg.value.decode())
            name = msg.key.decode()
            size = value['size']
            data = value['data']
            await save_file(name, data)
            await save_meta(name, size)
    except asyncio.CancelledError:
        pass


async def consume_file(consumer):
    try:
        async for msg in consumer:
            await comparison_result(msg)
    except asyncio.CancelledError:
        pass
