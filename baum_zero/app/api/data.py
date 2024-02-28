from app.kafka.producer import send_data
from app.services.bd import get_metadata
from bitstring import Bits, BitArray
from fastapi import APIRouter, status
from fastapi import File, UploadFile

router = APIRouter(
    prefix="/data",
    tags=["Data"],
)


@router.get("", status_code=status.HTTP_200_OK, response_model=dict)
async def get_data():
    list_metadata = {}
    total_size = 0
    metadata = await get_metadata()
    for i in metadata:
        list_metadata[i.id] = {'name': i.name, 'size': i.size}
        total_size += i.size
    out_data = {'total_size': total_size, 'list_metadata': list_metadata}
    return out_data


@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile = File(...)):
    read_file = await file.read()
    bits = Bits(BitArray(read_file))
    zero_count = bits.count(0)
    data_to_app_one = {
        "data": read_file,
        "count_zero": zero_count,
        "size": file.size,
    }
    await send_data(
        "files_to_one",
        file.filename.encode(),
        bytes(str(data_to_app_one), 'utf-8')
    )
    return {"message": "File uploaded successfully"}
