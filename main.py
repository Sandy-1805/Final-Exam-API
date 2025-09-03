from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/health")
async def health():
    return {message: "OK"}

@app.post("/phones")
async def phones():
    {identifier: str,
     brand: str,
     model: str,
     characteristics: {
         ram_memory: int,
         rom_memory: int
     }}
    status_code = 201
    
@app.get("/phones")
async def get_phones():
    return [{identifier: str,
             brand: str,
             model: str,
             characteristics: {
                 ram_memory: int,
                 rom_memory: int
             }}]

@app.get("/phones/{identifier}")
async def get_phone(identifier: str):
    return {identifier: str,
            brand: str,
            model: str,
            characteristics: {
                ram_memory: int,
                rom_memory: int
            }}

@app.put("/phones/{identifier}")
async def update_phone(identifier: str):
    {characteristics: {
         ram_memory: int,
         rom_memory: int
     }}
    return {identifier: str,
            brand: str,
            model: str,
            characteristics: {
                ram_memory: int,
                rom_memory: int
            }}