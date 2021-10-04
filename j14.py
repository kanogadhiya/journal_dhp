import matplotlib.pyplot as plot
import pandas as pd

data=pd.DataFrame({'Place':['Lodhika','Kalavad','Visavadar','Rajkot','Dhoraji','Kotdasangani','Jamkandorna','Paddhari','Gondal','Kapeada'],
'Rainfall (in mm)':[516,406,368,323,233,190,182,177,176,138]})

data.plot.bar(x='Place',y='Rainfall (in mm)',title="Bar Chart of a pandas DataFrame",color='orange')
plot.show()
