import pandas as pd
import numpy as np
import os
import glob
from concurrent.futures import ProcessPoolExecutor


def process_file(file_path, file_id):
    file_number = os.path.splitext(os.path.basename(file_path))[0]
    # Assuming space-separated values
    data = pd.read_csv(file_path, delim_whitespace=True)
    data = data[data["state"] == "transp"]
    data["year"] = data["time"] / (3600 * 24 * 365)
    data.rename(columns={"C.4.": "C(4)"}, inplace=True)

    # Filter and calculate avg_calcite for soln 1 to 10
    calcite_avg = data[data["soln"].between(1, 10)]["Calcite"].mean()
    data["avg_calcite"] = np.where(
        data["soln"].between(1, 10), calcite_avg, data["Calcite"]
    )

    # Convert from mole/liter to ton CO2/Ha
    conversion_factor = 500000 * 44 / 1000000
    data["Calcite"] = (
        data["avg_calcite"]
        * conversion_factor
        / data["soln"].apply(lambda x: 1 if x in range(1, 11) else 10)
    )
    data["C(4)"] = data["C(4)"] * conversion_factor / 10
    data["file_id"] = file_id

    return data[["soln", "Calcite", "Sr", "C(4)", "year", "file_id"]]


def process_all_files(base_path):
    folders = [f.path for f in os.scandir(base_path) if f.is_dir()]
    all_data = pd.DataFrame()

    with ProcessPoolExecutor() as executor:
        results = []
        file_id = 1
        for folder in folders:
            file_paths = glob.glob(os.path.join(folder, "*.out"))
            for file_path in file_paths:
                results.append(executor.submit(
                    process_file, file_path, file_id))
                file_id += 1

        for future in concurrent.futures.as_completed(results):
            all_data = pd.concat(
                [all_data, future.result()], ignore_index=True)

    return all_data


base_path = ""  # Get the path for data
all_data = process_all_files(base_path)
all_data.to_csv("all_data_6930.csv", index=False)
