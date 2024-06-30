import scipy.io
import pandas as pd
import numpy as np

# File paths
data_file = "F:\\CSE sem8\\bioinformatics\\prjct\\new_data\\dataset_4802.mat" #r"F:\\CSE sem8\\bioinformatics\\prjct\\new_data\\dataset_3106.mat"
y_file =  "F:\\CSE sem8\\bioinformatics\\prjct\\new_data\\Y_4802.mat" #r"F:\\CSE sem8\\bioinformatics\\prjct\\new_data\\Y_3106.mat"
output_csv = r"F:\\CSE sem8\\bioinformatics\\prjct\\new_data\\merged_data2.csv"

# Load .mat files
data_mat = scipy.io.loadmat(data_file)
y_mat = scipy.io.loadmat(y_file)

# Print keys
print("Keys in dataset_3106.mat:", data_mat.keys())
print("Keys in Y_3106.mat:", y_mat.keys())

# Function to get the main data array from a .mat file
def get_main_data(mat_dict):
    for key in mat_dict.keys():
        if isinstance(mat_dict[key], np.ndarray) and mat_dict[key].ndim >= 2:
            return mat_dict[key]
    return None

# Get main data arrays
data_array = get_main_data(data_mat)
y_array = get_main_data(y_mat)

if data_array is not None and y_array is not None:
    # Convert to DataFrames
    df_data = pd.DataFrame(data_array)
    df_y = pd.DataFrame(y_array)

    # Merge DataFrames
    merged_df = pd.concat([df_data, df_y], axis=1)

    # Save to CSV
    merged_df.to_csv(output_csv, index=False)

    print(f"Merged data saved to {output_csv}")
    print(f"Shape of merged data: {merged_df.shape}")
else:
    print("Could not find appropriate data arrays in the .mat files.")