from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter


#########################
# BLOCK WITH API ROUTES #
#########################
# create instance of the app
app = FastAPI(title="luchanos-oxford-university")

user_router = APIRouter()


# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="localhost", port=8000)
