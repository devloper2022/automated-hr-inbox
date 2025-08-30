import glob
from resume_parser import parse_resume
from rating import rate_candidate
from save_excel import save_to_excel

# For demonstration, use sample resumes
sample_files = glob.glob("sample_resumes/*")

candidates = []
for file in sample_files:
    data = parse_resume(file)
    data["Rating"] = rate_candidate(data)
    candidates.append(data)

save_to_excel(candidates)
