HR Automation: Inbox Scanning & Applicant Rating
Project Overview

This project automates the HR process of collecting, parsing, and rating job applicants’ resumes. It allows HR teams to:

Fetch resumes from Gmail (optional).

Extract applicant information from PDF or DOCX resumes:

Name

Email

Phone number

Skills (Python, Java, C++, AWS, SQL, ML)

Work experience (in years)

Automatically rate applicants based on experience.

Store all results in an Excel file (candidates.xlsx) for easy review.

This saves HR teams significant time and provides a structured way to compare applicants.

Features

Resume Parsing: Works for PDF and DOCX formats.

Skill Extraction: Detects key technical skills from resumes.

Experience Rating:

0–1 year → Beginner (1⭐)

2–4 years → Intermediate (2⭐)

5+ years → Experienced (3⭐)

Excel Export: Generates a ready-to-use Excel sheet with all candidate data.

Optional Gmail Integration: Automatically fetch resumes from Gmail attachments.

Repository Structure
HR-Automation/
│
├─ README.md                  # Project description
├─ requirements.txt           # Python dependencies
├─ main.py                    # Main execution script
├─ gmail_fetch.py             # Gmail fetch functionality (optional)
├─ resume_parser.py           # Resume parsing functions
├─ rating.py                  # Candidate rating logic
├─ save_excel.py              # Excel export logic
├─ sample_resumes/            # Sample resumes for testing
│     ├─ resume1.pdf
│     ├─ resume2.docx

Setup Instructions
1. Install Dependencies
pip install -r requirements.txt


Dependencies include:

pdfplumber → PDF parsing

python-docx → DOCX parsing

openpyxl → Excel file handling

pandas → Data manipulation

google-auth & google-api-python-client → Gmail integration (optional)

2. Prepare Sample Resumes

Place sample resumes in the folder sample_resumes/ (PDF or DOCX).
These will be parsed and rated by the script.

3. Run the Script

Run the main script to parse resumes and generate Excel output:

python main.py


The script will read all resumes in sample_resumes/

Parse information and rate applicants

Save results in candidates.xlsx

4. Gmail Integration (Optional)

If you want to automatically fetch resumes from Gmail:

Create a Google Cloud OAuth client ID (Desktop App).

Download credentials.json (do not upload this to GitHub).

Place credentials.json in your Colab or local directory.

Use gmail_fetch.py to download attachments from your inbox:

from gmail_fetch import fetch_emails_and_download

files = fetch_emails_and_download(service)


These downloaded files can then be parsed using resume_parser.py.

5. Output

Excel file: candidates.xlsx

Columns: Name, Email, Phone, Skills, Experience, Resume File, Rating

This file is ready for HR review.

Notes & Safety

Do not upload credentials.json to GitHub – it contains sensitive Gmail access.

Include only the notebook or Python scripts for GitHub submission.

The sample resumes in sample_resumes/ demonstrate the functionality.
