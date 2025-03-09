# FastAPI Course Generator

This project is a FastAPI-based backend that generates structured course outlines based on user input. It utilizes Google Generative AI (Gemini 1.5) for course content generation and Google Custom Search API for fetching relevant references.

## Features
- **FastAPI**: A high-performance Python web framework.
- **Google Generative AI (Gemini 1.5)**: Generates course outlines based on structured prompts.
- **Google Custom Search API**: Retrieves relevant references for course content.
- **Modular Structure**: Divided into services, routes, and main application logic.
- **Environment Configuration**: Uses `.env` files for managing API keys securely.

## Project Structure
```
my_project/
├── app/
│   ├── main.py  # Entry point for FastAPI application
│   ├── routes/
│   │   ├── course_routes.py  # API routes for course generation
│   ├── services/
│   │   ├── course_service.py  # Handles course generation logic
│   │   ├── search_service.py  # Performs web search using Google API
│   ├── models/
│   │   ├── course_request.py  # Pydantic model for course request validation
│   ├── utils/
│   │   ├── helpers.py  # Helper functions
├── .env  # Stores API keys (not included in Git)
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
```

## Installation

### Prerequisites
- Python 3.10+
- `pip` installed
- Google API keys for Generative AI and Custom Search

### Steps
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd my_project
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory and add the following:
     ```env
     API_KEY=<your-google-generative-ai-api-key>
     SEARCH_API_KEY=<your-google-custom-search-api-key>
     CSE_ID=<your-custom-search-engine-id>
     ```
5. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

### API Endpoints
#### 1. Generate Course
- **Endpoint:** `POST /generate_course`
- **Request Body:**
  ```json
  {
    "brief": "A microfinance course for beginners who need to learn from basics",
    "target_audience": "College students with no financial background",
    "course_duration": "6 weeks"
  }
  ```
- **Response:**
  ```json
  {
    "course_title": "Microfinance Basics",
    "description": "A beginner-friendly course on microfinance principles...",
    "modules": [...],
    "references": [...]
  }
  ```

### Testing
You can test the API using Postman or directly via FastAPI's interactive docs at:
```
http://127.0.0.1:8000/docs
```

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork, open issues, or submit PRs to enhance functionality!

---

This `README.md` provides all necessary setup and usage details. Let me know if you need modifications!

