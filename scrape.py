import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
app = FastAPI()

# Function to extract clean text content from the HTML preserving alignments and write it to a file with a maximum size limit
def extract_clean_text_and_write_to_file(url, max_file_size=25 * 1024 * 1024):
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text from HTML preserving structure and formatting
        text_content = soup.get_text(separator='\n')

        return text_content
    else:
        return response.status_code,


@app.get("/get_content")
def get_content(Body:dict):
    URL = Body.get("URL")
    content=extract_clean_text_and_write_to_file(URL)
    return {
            "content": content,
        }

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)