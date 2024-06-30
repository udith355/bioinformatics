import pandas as pd
import os

# Define input file paths
file1 = r"F:\\CSE sem8\\bioinformatics\\prjct\\processed_data\\deeploc_extracted.csv"
file2 = r"F:\\CSE sem8\\bioinformatics\\prjct\\processed_data\\multisub_extracted.csv"

# Define output file path
output_dir = r"F:\\CSE sem8\\bioinformatics\\prjct\\merged_data"
output_file = os.path.join(output_dir, "combined_data.csv")

# Read the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine the dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicates based on 'ID' column, keeping the first occurrence
combined_df.drop_duplicates(subset='ID', keep='first', inplace=True)

# Ensure only 'ID' and 'Sequence' columns are present
combined_df = combined_df[['ID', 'Sequence']]

# Write the result to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f"Combined data with unique IDs saved to {output_file}")
print(f"Total number of unique entries: {len(combined_df)}")