import asyncio

import uvicorn
from aiokafka import AIOKafkaConsumer
from app.api.routers import all_routers
from app.kafka.consumer import consume_file, consume_file_meta_save
from fastapi import FastAPI

app = FastAPI(title='baum_zero')

for router in all_routers:
    app.include_router(router)


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    consumer_files_to_zero = AIOKafkaConsumer(
        'files_to_zero', loop=loop, bootstrap_servers='kafka1:9092'
    )
    consumer_save_file_to_zero = AIOKafkaConsumer(
        'save_file_to_zero', loop=loop, bootstrap_servers='kafka1:9092'
    )
    await consumer_files_to_zero.start()
    await consumer_save_file_to_zero.start()
    asyncio.create_task(consume_file(consumer_files_to_zero))
    asyncio.create_task(consume_file_meta_save(consumer_save_file_to_zero))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
