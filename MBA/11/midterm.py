import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('midterm.csv')
x=pd.cut(df['Midterm'],[0,59,69,79,89,100],labels=['F','D','C','B','A'])
y=x.groupby(x).count()
plt.bar(y.index, y.values)
plt.savefig('midterm.jpg',dpi=300)