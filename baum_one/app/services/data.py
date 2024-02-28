from typing import Any

from app.kafka.producer import send_data
from app.services.bd import save_meta
from app.services.file import save_file
from bitstring import Bits, BitArray


async def comparison_result(msg: Any) -> None:
    value = eval(msg.value.decode())
    name = msg.key.decode()
    bits = Bits(BitArray(value['data']))
    one_count = bits.count(1)
    if one_count > value['count_zero']:
        await save_file(name, value)
        await save_meta(name, value)
    elif one_count == value['count_zero']:
        await save_file(name, value)
        await save_meta(name, value)
        await send_data("save_file_to_zero", msg.key, msg.value)
    else:
        await send_data("save_file_to_zero", msg.key, msg.value)
