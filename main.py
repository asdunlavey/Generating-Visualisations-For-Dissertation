import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#me mehdi stephan aaron Leo Ryan

def create_df(url=None) -> pd.DataFrame:
    if url is None: raise Exception('A url must be passed')
    df: pd.DataFrame = pd.read_csv(url)
    head: int = 5  # Visualises the n most common entire
    head = min(head, df.shape[0])  # Prevents crashing if 'head' exceeds shape
    df = df.nlargest(head, 'Quantity')
    return df


def create_pie_chart(df=None) -> None:
    if df is None: raise Exception('A DataFrame must be passed.')
    x = np.array(df['Service'])  # labels
    y = np.array(df['Quantity'])  # slices
    colours = np.array(df['Colour'])  # slice colours
    explode = [0.1] + [0]*(df.shape[0] - 1)  # biggest slice slightly pops out
    plt.pie(y, labels=x, autopct='%1.1f%%', explode=explode, colors=colours)
    plt.show()


if __name__ == '__main__':
    csv_url: str = 'streaming_services.csv'
    DataFrame = create_df(csv_url)
    create_pie_chart(DataFrame)
