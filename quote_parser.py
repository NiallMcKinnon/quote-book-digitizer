import re
import csv


IN_FILE = "./raw_quotes/Quotes.txt"
OUT_FILE = "./output/Quotes.csv"
EXCEPTIONS_FILE = "./output/Quotes_err.txt"

with open(IN_FILE, "r") as file:
    lines = [line for line in file if line != "\n"]
    
matched_lines = []
unmatched_lines = []
    
for i, line in enumerate(lines):
    match = re.search(r'[\"|”|“](.*)[\"|”|“]\s+[–—-]\s+([\w+\s?]+),?\s+(\d+/\d+/\d+)', line)
    if match:
        matched_lines.append([match.group(1), match.group(2), match.group(3)])
    else:
        unmatched_lines.append(line)
        
with open(OUT_FILE, "w") as good_csvfile:
    good_writer = csv.writer(good_csvfile)
    good_writer.writerows(matched_lines)
    
with open(EXCEPTIONS_FILE, "w") as exceptions_file:
    exceptions_file.writelines(unmatched_lines)