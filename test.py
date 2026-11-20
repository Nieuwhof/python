
# Data
file_list = ["file1.csv", "file2.csv", "file3.csv", "file1.csv"]
processed = []

n = 0

for file in file_list:
    if file not in processed:
        processed.append(file)
        n += 1
        print(f"Processing {file}...")
    else:
        print(f"{file} has already been processed. Skipping.")






