import matplotlib.pyplot as plot
import pandas as pd

data=pd.DataFrame({'x':[10,20,30,40,50,60,70,80,90,100],
'y':[553,335,554,873,355,955,260,803,605,343]})

data.plot.line(x='x',y='y',xlabel='X axis',ylabel='Y axis',title="Pandas Data Frame to Line chart .")
plot.show()

# data.plot.line(x='x',y='y',color='purple')
# plot.xlabel('X axis')
# plot.ylabel('Y axis')
# plot.title('Pandas Data Frame to Line chart .')
# plot.show()