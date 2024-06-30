import csv
import pandas as pd
import os

# Input FASTA file path
fasta_file = r"F:\\CSE sem8\bioinformatics\\prjct\\deeploc1\\deeploc_data.fasta"

# Output CSV file path
output_dir = r"F:\\CSE sem8\bioinformatics\\prjct\\original_data"
csv_file = os.path.join(output_dir, "deeploc_data.csv")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read FASTA and convert to DataFrame
data = []
with open(fasta_file, 'r') as file:
    header = ""
    sequence = ""
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if header:
                data.append(header.split() + [sequence])
            header = line[1:]  # Remove the '>' character
            sequence = ""
        else:
            sequence += line
    if header:
        data.append(header.split() + [sequence])

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv(csv_file, index=False, header=False)

print(f"FASTA file converted to CSV: {csv_file}")