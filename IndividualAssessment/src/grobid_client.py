import requests
import os
import logging

GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

def process_papers(pdf_folder):
    """Send PDFs to GROBID for processing and return the extracted text."""
    processed_papers = {}

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(pdf_folder, filename)
            logging.info(f"Processing: {filename}")

            with open(filepath, "rb") as pdf:
                response = requests.post(
                    GROBID_URL, 
                    files={"input": pdf}, 
                    data={"consolidateHeader": 1}
                )
                
                if response.status_code == 200:
                    processed_papers[filename] = response.text
                else:
                    logging.error(f"Processing error: {filename}")

    return processed_papers
