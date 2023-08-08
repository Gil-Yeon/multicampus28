import pandas as pd

def main():
    data = pd.read_json("popluation.json")
    df = pd.DataFrame(data)

    print(df.head())

if __name__ == "__main__":
    main()