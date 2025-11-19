import pandas as pd
import numpy as np
from math import sqrt
from scipy import stats

def calc_4m(df, column_name):
    """
    Returnerar en disctionary med beräkning av median, mean, min och max
    """
    calculated = pd.DataFrame({
        "median" : df[column_name].median(),
        "mean" : df[column_name].mean(),
        "min" : df[column_name].min(),
        "max" : df[column_name].max()
    })
    return calculated.round(2)


def calc_percentage(df, column_name):
    """
    Returnerar procentuella fördelningen för varje unikt värde i den kolumn du väljer
    """
    counter = df.groupby(column_name).size()
    tot_people = len(df)
    percentage = (counter / tot_people) * 100
    
    return percentage.round(2)

#tagit kod från lektionen om konfidensintervall
def ci_mean_normal(x, confidence=0.95):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    
    mean_x = float(np.mean(x))
    s = float(np.mean(x))
    s = float(np.std(x, ddof=1))
    n = len(x)
    z_critical = 1.96
    half_width = z_critical * s / sqrt(n)

    lo = mean_x - half_width
    hi = mean_x + half_width
    return lo, hi, mean_x, s, n

#tagit kod från lektionen om konfidensintervall
def ci_mean_bootsrap(x, B=500, confidence=0.95):
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    boot_means = np.empty(B)
    for b in range(B):
        boot_sample = np.random.choice(x, size=n, replace=True)
        boot_means[b] = np.mean(boot_sample)
    
    alpha = (1 - confidence) / 2
    lo = np.percentile(boot_means, 100*alpha)
    hi = np.percentile(boot_means, 100*(1 - alpha))

    return float(lo), float(hi), float(np.mean(x)), boot_means


def test_smoker_bp(df):
    """
    Hypotesprövning: Rökare har högre systoliskt blodtryck än icke rökare
    """
    smoker_col = df["smoker"].astype(str).str.strip().str.lower()
    smokers = df.loc[smoker_col == "yes", "systolic_bp"].dropna().values
    non_smokers = df.loc[smoker_col == "no", "systolic_bp"].dropna().values
    mean_smokers = float(np.mean(smokers))
    mean_non_smokers = float(np.mean(non_smokers))
    diff_mean = mean_smokers - mean_non_smokers

    t_stat, p_two = stats.ttest_ind(smokers, non_smokers, equal_var=False)

    if t_stat > 0:
        p_one = p_two / 2
    else:
        p_one = 1 - p_two / 2

    return (mean_smokers, mean_non_smokers, diff_mean, t_stat, p_one, smokers, non_smokers)
    