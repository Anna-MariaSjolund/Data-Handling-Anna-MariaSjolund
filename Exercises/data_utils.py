import seaborn as sns
import pandas as pd

def plot_missing(dataframe, bars_at_x_axis=True):
    nulls_count = pd.DataFrame({"Variables":dataframe.columns, "Count":dataframe.isnull().sum()}).reset_index(drop=True)
    nulls_count = nulls_count[nulls_count["Count"] > 0]
    if bars_at_x_axis == True:
        sns.barplot(data=nulls_count, x="Variables", y="Count").set_title("Null Values")
    else:
        sns.barplot(data=nulls_count, x="Count", y="Variables").set_title("Null Values")