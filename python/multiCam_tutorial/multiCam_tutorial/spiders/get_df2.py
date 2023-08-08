import pandas as pd

def main():
    data = pd.read_csv('popluation.csv')
    df = pd.DataFrame(data)

    print(df.head())

if __name__ == '__main__':
    main()