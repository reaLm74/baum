import os


async def save_file(name, data) -> None:
    file_path = os.path.join("files", name)
    with open(file_path, "wb") as f:
        f.write(data)
