from datasets import load_dataset
import json
import os
import sys
import pandas as pd


def load_bigcodebench():
    # Load dataset (use streaming for large datasets)
    splits = {'v0.1.0_hf': 'data/v0.1.0_hf-00000-of-00001.parquet', 'v0.1.1': 'data/v0.1.1-00000-of-00001.parquet', 'v0.1.2': 'data/v0.1.2-00000-of-00001.parquet', 'v0.1.3': 'data/v0.1.3-00000-of-00001.parquet', 'v0.1.4': 'data/v0.1.4-00000-of-00001.parquet'}
    df = pd.read_parquet("hf://datasets/bigcode/bigcodebench/" + splits["v0.1.0_hf"])
    # print (type(ds))
    return df

def load_column(column_name: str, output_dir: str, dataset: pd.DataFrame):
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    print(f"Extracting column: '{column_name}'")
    print(f"Saving files to: {output_dir}/")

    # Check if column exists in dataframe
    if column_name not in dataset.columns:
        print(f"Error: Column '{column_name}' not found in dataframe")
        print(f"Available columns: {list(dataset.columns)}")
        return

    # Extract column values
    for i, value in enumerate(dataset[column_name]):
        # Create filename
        filename = f"{output_dir}/{column_name}_{i:04d}.txt"
        
        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            if isinstance(value, (dict, list)):
                json.dump(value, f, indent=2)
            else:
                f.write(str(value))
        
        print(f"Saved: {filename}")

    print(f"\nDone! Extracted {len(dataset)} files.")


if __name__ == "__main__":

    directory = sys.argv[2]
    column = sys.argv[1]
    dataset = load_bigcodebench()
    load_column(column, directory, dataset)