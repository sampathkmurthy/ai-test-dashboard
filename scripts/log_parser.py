import re
import pandas as pd

def parse_log(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    errors = [line for line in lines if "ERROR" in line]
    df = pd.DataFrame(errors, columns=["Error Lines"])
    print(df)

if __name__ == "__main__":
    parse_log("sample.log")
