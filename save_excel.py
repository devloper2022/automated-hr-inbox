import pandas as pd
import os

def save_to_excel(candidates, excel_file="candidates.xlsx"):
    df = pd.DataFrame(candidates)
    if os.path.exists(excel_file):
        old = pd.read_excel(excel_file)
        df = pd.concat([old, df], ignore_index=True)
    df.to_excel(excel_file, index=False)
    print(f"Saved {len(candidates)} candidates to {excel_file}")
