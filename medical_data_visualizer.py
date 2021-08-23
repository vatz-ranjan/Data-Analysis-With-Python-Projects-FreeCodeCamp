import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = df["weight"] / ((df["height"]/100)**2)
df.loc[df['overweight'] <= 25, 'overweight'] = 0
df.loc[df['overweight'] > 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] <= 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] <= 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars= ["cardio"], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(
        df_cat.groupby(['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    # Draw the catplot with 'sns.catplot()'
    figure = sns.catplot(data = df_cat, x='variable', y='total', hue='value', col='cardio', kind="bar")

    fig = figure.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corre = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corre, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10,12))

    # Draw the heatmap with 'sns.heatmap()'
    figure = sns.heatmap(corre, annot=True, fmt='.1f', mask=mask, vmin=-0.08, vmax=0.24, center=0.08, square=True, linewidths=.5, cbar_kws={'shrink':.4, 'format':'%.2f'})
    fig = figure.get_figure()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

