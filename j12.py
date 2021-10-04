import matplotlib.pyplot as plot
import pandas as pd

df=pd.DataFrame({'Roll no.':[1,2,3,4,5,6,7,8,9,10],
'Marks (in 10)':[54,35,54,87,35,95,20,80,65,43]})


# df.plot.scatter(x='Roll no.',y='Marks (in 10)',color='purple',title="Data Frame to Scatter chart .")
# plot.show()

df.plot.scatter(x='Roll no.',y='Marks (in 10)',color='purple')
plot.title('Data Frame to Scatter chart .')
plot.show()