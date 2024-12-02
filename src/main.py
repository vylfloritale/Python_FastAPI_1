from fastapi import FastAPI
from api import get_known, info, get_all, get_new, get_query_key

app = FastAPI()

app.include_router(info.router)
app.include_router(get_all.router)
app.include_router(get_new.router)
app.include_router(get_known.router)
app.include_router(get_query_key.router)