
##### Code that is re-used over multiple assignments in Econ 570 will be placed in
# this module for easy import into future assignments.
#####

import pandas as pd


def summary_statistics(_df: pd.DataFrame, stats_col_name: str, date_col_name: str) -> dict:

    """
    Use this function to find the summary statistics discussed in the Econ 570 slides, "Lecture2_SP2026.pdf".

    Parameters
    ----------
    _df : pd.DataFrame
        Passed DataFrame containing stats_col_name and date_col_name.
    stats_col_name : str
        Column on which to calculate the summary statistics.
    date_col_name : str
        Column on which to find min and max date.

    Returns
    -------
    dict
        Key 'df_summary_stats' contains the DataFrame of summary statistics.
        Key 'min_date' is the minimum of date_col_name.
        Key 'max_date' is the maximum of date_col_name.

    """

    # Added this for when the date column was set as the index.
    _df = _df.reset_index()

    df_summary_stats = pd.DataFrame(
    data={
        'mean': [_df[stats_col_name].mean()],
        'median': [_df[stats_col_name].median()],
        'var': [_df[stats_col_name].var()],
        'std_dev': [_df[stats_col_name].std()],
        'skewness': [_df[stats_col_name].skew()],
        'kurtosis': [_df[stats_col_name].kurtosis()]
        }
    ).T\
    .reset_index(names='statistic')\
    .rename(columns={0: 'value'}, errors='raise')\
    .round(4)

    return {
        'df_summary_stats': df_summary_stats,
        'min_date': _df[date_col_name].min(),
        'max_date': _df[date_col_name].max()
        }
