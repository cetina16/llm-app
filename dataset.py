import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df['source_text'].tolist(), df['target_text'].tolist()
