import json
import re
from app.services.search_service import perform_web_search
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI API with the API key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the Google Generative AI model
generative_model = genai.GenerativeModel('gemini-1.5-flash')

def generate_course_content(user_input: dict):
    """
    Generate a structured course outline based on user input and web search results.
    """
    brief = user_input['brief']
    target_audience = user_input['target_audience']
    course_duration = user_input['course_duration']

    # Perform web search to gather resources
    search_query = f"course on {brief} for {target_audience}"
    web_search_results = perform_web_search(search_query)

    # Format search results for the prompt
    web_results_str = "\n".join(
        [f"- {result['title']}: {result['snippet']} (Link: {result['link']})"
         for result in web_search_results]
    )

    # Generate user query for AI model
    user_query = (
        f"""
        You are an AI assistant specializing in educational course generation. Provide structured and well-researched responses.
        Here are some web search results related to the course topic:
        {web_results_str}
        
        Now, generate a structured course outline in JSON format based on the following input:
            - Course Brief: {brief}
            - Target Audience: {target_audience}
            - Course Duration: {course_duration}
        
        The output should include:
            - course_title: The title of the course
            - description: A brief description of the course
            - modules: A list of modules, each containing:
                - title: The title of the module
                - lessons: A list of lessons, each containing:
                    - title: The lesson title
                    - content: The content of the lesson
                    - resources: A list of references or resources
            - references: A list of sources or references related to the course
        Please return only the JSON formatted response with no extra text.
        """
    )

    # Generate the response from the AI model
    history = [{"role": "user", "parts": [user_query]}]
    response = generative_model.generate_content(history).text

    # Extract and return the JSON formatted course content
    pattern = r'```json\n([\s\S]*?)\n```'
    formatted_data = re.search(pattern, response)

    if formatted_data:
        json_string = formatted_data.group(1).strip()
        course_content = json.loads(json_string)
        return course_content
    else:
        return {"Error": "No response was generated by Gemini API"}
