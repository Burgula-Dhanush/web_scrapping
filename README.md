
```markdown
# 🌐 Web Scraping and Text Extraction with FastAPI

This Python script uses FastAPI to create a web service that extracts clean text content from a webpage while preserving alignments. The extracted content is returned as a response when calling the `/get_content` endpoint.

## 🛠️ Requirements

- Python 3.x
- `requests` library: Used for making HTTP requests.
- `beautifulsoup4` library: Used for parsing HTML content and extracting text.
- `fastapi` library: Used for creating the web service.

You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4 fastapi uvicorn
```

## ▶️ Usage

1. Clone or download the script file (`scrape.py`) to your local machine.

2. Run the FastAPI app using the following command:

```bash
uvicorn scrape:app --reload
```

3. Access the FastAPI documentation at `http://localhost:8000/docs` to interact with the `/get_content` endpoint.

4. Enter the URL in the provided form and execute to get the extracted clean text content.

## 🌟 Example

```bash
curl -X 'GET' \
  'http://localhost:8000/get_content?URL=[URL_of_the_webpage]' \
  -H 'accept: application/json'
```

## 📝 Note

- The extracted text content will be returned as a response to the `/get_content` endpoint.
- The FastAPI app also has a default `/` endpoint that returns a simple "Hello World" message.

Feel free to customize and use this script to build upon your web scraping projects!
```
