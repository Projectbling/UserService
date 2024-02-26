from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Config.DatabaseConfig import init_db
import uvicorn
from MODULES.User.url import guest_router



app = FastAPI()
init_db(app)

app.include_router(guest_router)


@app.get("/")
async def read_root():     
    return JSONResponse(content={"message": "Hello, World"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)