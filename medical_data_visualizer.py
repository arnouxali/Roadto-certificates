import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['bmi']=df['weight']/((df['height']/100)**2)
df['overweight'] = df['bmi'].apply(lambda x: 1 if x > 25 else 0)
df.drop(columns='bmi', inplace=True)


# 3
df['cholesterol']=df['cholesterol'].apply(lambda x:0 if x==1 else 1)
df['gluc']=df['gluc'].apply(lambda x:0 if x==1 else 1)

# 4
def draw_cat_plot():
    # 5

    df_cat = df.melt(id_vars=['cardio'], value_vars=['alco', 'overweight', 'smoke', 'gluc', 'cholesterol', 'active'],
                      var_name='variable', value_name='value')



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # 7
    sns.set_style('white')
    sns.set_context('paper', font_scale=1.2)
    catplot = sns.catplot(data=df_cat, x='variable', y='total', kind='bar', hue='value', col='cardio',
                          palette='seismic')
    plt.legend(loc=0)


    # 8
    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_hi'] >= df['ap_lo'])&(df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (
                df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()


    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10,10))

    # 15

    sns.heatmap(mask=mask, data=corr,ax=ax,cmap='BrBG',center=0,annot=True,fmt=".1f", linewidths=0.6, linecolor='white',square=True,annot_kws={"size": 12})
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=12)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=12)
    # 16
    fig.savefig('heatmap.png')
    return fig

