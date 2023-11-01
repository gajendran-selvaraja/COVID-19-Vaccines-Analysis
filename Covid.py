import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
PATH = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
df_w = pd.read_csv(PATH)
df_w = df_w[df_w.date <= '2021-12-08']
print("The DataFrame has:",
      "\nNumber of rows:",df_w.shape[0],
      "\nand",df_w.shape[1], "number of columns"
      )
df_w.head()
df_w.tail()
df_w.columns.to_list()
round((df_w.isnull().sum()/df_w.shape[0]).sort_values(ascending=False),3)
sns.set_style('ticks')
fig, ax = plt.subplots(figsize=(14,8))

# Build the variable for the top 5 countries
tc_5 = (df_w.loc[(df_w.date =='2021-12-08') & df_w.continent.notnull()].sort_values(by = 'total_cases', ascending = False)[:5].copy())

# Calling the plot
bar_plot = sns.barplot(x = 'total_cases' , y = 'location' ,data = tc_5, orient = 'h',ax = ax, color = "#357599")

# Customizing the plot
for p in bar_plot.patches:
    width=int(p.get_width())
    plt.text(p.get_width(), p.get_y()+0.55*p.get_height(),
            '{}'.format(width),
             ha='right', va='center', color='white', size=16, fontweight='bold')
 
ax.set_title('The five countries with the highest numbers of total cases\n', loc='left', size=22, color='DarkSlateGray')
ax.set_xlabel([], color='white')
ax.set_ylabel([], color='white')
ax.set_xticklabels([],color = 'whiite')
ax.set_yticklabels(["EUA","IND","BRA","GBR",'RUS'],{'fontsize': 16, 
 'verticalalignment': 'baseline'})
sns.despine(left=True, bottom=True)


plt.tight_layout()
