import pandas as pd
import os

# Define input file paths
file1 = r"F:\\CSE sem8\\bioinformatics\\prjct\\original_data\\deeploc_data.csv"
file2 = r"F:\\CSE sem8\\bioinformatics\\prjct\\original_data\\multisub_5_partitions_unique.csv"

# Define output file paths
output_dir = r"F:\\CSE sem8\\bioinformatics\\prjct\\processed_data"
output1 = os.path.join(output_dir, "deeploc_extracted.csv")
output2 = os.path.join(output_dir, "multisub_extracted.csv")

# Process deeploc_data.csv
df1 = pd.read_csv(file1)
df1[['ID', 'Sequence']].to_csv(output1, index=False)

# Process multisub_5_partitions_unique.csv
df2 = pd.read_csv(file2)
df2[['ID', 'Sequence']].to_csv(output2, index=False)

print(f"Extracted data saved to {output1} and {output2}")