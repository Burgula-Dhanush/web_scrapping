# 🌐 Web Scraping and Text Extraction Script

This Python script extracts clean text content from a webpage while preserving alignments and writes it to a file with a specified maximum size limit.

## 🛠️ Requirements

- Python 3.x
- `requests` library: Used for making HTTP requests.
- `beautifulsoup4` library: Used for parsing HTML content and extracting text.

You can install the required libraries using the following command:

bash
pip install requests beautifulsoup4

▶️ Usage
Clone or download the script file (scrape.py) to your local machine.

Run the script using the following command:

bash
python scrape.py
Follow the prompts to input the URL of the webpage, the output directory path, and the output file name.

The script will extract clean text content from the specified URL, preserving alignments, and write it to the specified output file.

🌟 Example
bash
python scrape.py


📝 Note
The extracted text content will be written to a file in the specified output directory.
If the file size exceeds the maximum limit (default: 25 MB), the extraction process will stop, and a message will be displayed.

