import matplotlib.pyplot as plot
import pandas as pd

df= pd.DataFrame({'Endlish':[50,63,43,70],
'Maths':[70,50,60,40],
'Science':[43,56,40,65]},index=['yash','meet','riddhi','smit'])
print(df)

df.plot.barh(figsize=(8,7),rot=100,title="Compound horizontal bar chart using pandas DataFrame")
plot.legend(loc='lower right')
plot.show()