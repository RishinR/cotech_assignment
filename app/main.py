from fastapi import FastAPI
from app.routes.course_routes import router as course_router

# Initialize FastAPI app
app = FastAPI()

# Include course routes
app.include_router(course_router)

# Run the app using uvicorn:
# uvicorn app.main:app --reload
