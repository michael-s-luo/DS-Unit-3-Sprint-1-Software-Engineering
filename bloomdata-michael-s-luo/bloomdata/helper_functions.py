"""
Helper functions for Unit 3 Bloomdata package project
Name: Michael Luo
Date: 2022/11/10
"""

import random
import pandas as pd, numpy as np


def random_phrase():
    adjs = [
        "blue",
        "large",
        "grainy",
        "substantial",
        "potent",
        "thermonuclear",
    ]
    nouns = ["food", "house", "tree", "bicycle", "toupee", "phone"]

    return f"{random.choice(adjs)} {random.choice(nouns)}"


def random_float(min_val: float, max_val: float):
    return min_val + (random.random() * (max_val - min_val))


def random_bowling_score():
    return random.randint(0, 300)


def silly_tuple():
    return (
        random_phrase(),
        round(random_float(1, 5), 1),
        random_bowling_score(),
    )


def silly_tuple_list(num_tuples: int):
    return [silly_tuple() for _ in range(num_tuples)]


###ADVANCED HELPER FUNCTIONS FOR NUMPY, PANDAS #################################
"""As much 'vanilla' python as possible, with minimal calls to numpy and/or pandas"""


def null_count(df: pd.DataFrame) -> int:
    return df.isnull().sum().sum()


def get_hc_columns(df: pd.DataFrame, cutoff: int) -> list[str]:
    return [col for col, nunique in df.nunique().items() if nunique > cutoff]


def list_2_series(
    list_2_series: list, df: pd.DataFrame, name: str
) -> pd.DataFrame:
    df[name] = list_2_series

    return df


def split_dates(date_series: pd.Series):
    day = date_series.dt.day
    month = date_series.dt.month
    year = date_series.dt.year

    day.name = "day"
    month.name = "month"
    year.name = "year"

    return pd.concat([day, month, year], axis=1)


if __name__ == "__main__":
    # # silly_tuple_list test
    # print(silly_tuple_list(5))

    # # null_count test
    # df = pd.DataFrame({"test": [1, 2, np.NaN, np.NaN]})
    # print(null_count(df))
    ...
