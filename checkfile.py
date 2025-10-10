import pandas as pd

input_path = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WELL_TEST_WilliamsCo.rpt"
output_path = r"C:\Users\10216172\OneDrive - State of Ohio\Desktop\MS_UC\WilliamsCoWells\WELL_TEST_WilliamsCo.csv"
#Read the file
file = pd.read_csv(input_path, delim_whitespace=True)

column_to_skip = ''  # Replace with the actual column name

#Save new file
file.to_csv(output_path, index=False)

file_new = pd.read_csv(output_path)
print("Complete")
print(file_new)