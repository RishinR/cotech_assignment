from pydantic import BaseModel

class CourseRequest(BaseModel):
    brief: str  # Brief description of the course
    target_audience: str  # Target audience for the course
    course_duration: str  # Duration of the course
