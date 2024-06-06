from fastapi import APIRouter
from series.session import get_series, add_series
from fastapi import HTTPException
from series.schema import Series

route = APIRouter()

@route.get("/all")
async def all():
    series = await get_series()
    if not series:
        return HTTPException(status_code=404, message = 'series not found')
    return series

@route.post("/add-movies")
def add(series : Series):
    return add_series(series.title, series.date, series.season, series.link, series.country, series.image, series.rating)

