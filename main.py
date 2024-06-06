from fastapi import FastAPI
from kdramaapi import route

app = FastAPI()

app.include_router(route)

