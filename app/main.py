import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/eval")
async def eval_user_input(q: str):
    result = eval(q)  # vulnerable use of eval
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")