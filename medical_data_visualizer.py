import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)) > 25

# 3
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5  
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
        
    
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).value_counts()
    #print(df_cat)
    #type(df_cat)

    # 7
    #df_cat.explode(['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    thing = sns.catplot(data=df_cat, x='variable', y='count', col='cardio', kind='bar', hue='value', palette='pastel').set(ylabel='total')


    # 8
    fig = thing.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    #df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])].loc[(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['height'].quantile(0.025)) & (df['weight'] <= df['height'].quantile(0.975))]
    #df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])].loc[(df['height'] >= df['height'].quantile(0.025))].loc[(df['height'] <= df['height'].quantile(0.975))].loc[(df['weight'] >= df['height'].quantile(0.025))].loc[(df['weight'] <= df['height'].quantile(0.975))]
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))].copy()

    # 12
    corr = df_heat.corr()
    #sns.heatmap(corr).figure.savefig('corrmatrix.png')
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(data=corr, mask=mask, annot=True, fmt=".1f")

    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
