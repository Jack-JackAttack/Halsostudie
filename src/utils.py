import pandas as pd

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