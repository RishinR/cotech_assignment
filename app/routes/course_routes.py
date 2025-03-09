from fastapi import APIRouter, HTTPException
from app.services.course_service import generate_course_content
from app.models.course import CourseRequest

# Initialize router for course routes
router = APIRouter()

@router.post("/generate-course/")
async def generate_course(request: CourseRequest):
    """
    Endpoint to generate a course outline based on user input.
    """
    try:
        user_input = request.dict()  # Convert the incoming request to a dictionary
        course_content = generate_course_content(user_input)
        
        # If the response is an error, raise an HTTP exception
        if "Error" in course_content:
            raise HTTPException(status_code=500, detail=course_content["Error"])
        
        return course_content

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
