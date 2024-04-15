from api.handlers import user_router
from fastapi import FastAPI
from fastapi.routing import APIRouter


app = FastAPI(title="educational platform")
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)
