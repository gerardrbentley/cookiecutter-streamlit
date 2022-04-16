import pandas as pd


def add_answer(df: pd.DataFrame):
    out_df = df.copy()
    out_df["the_answer"] = 42
    return out_df
