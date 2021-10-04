import csv
import pandas as pd
df=pd.DataFrame({   "name":['yash','akash','dhruvi','meet','savan'],
                    "rollno":['101','102','103','104','105']
                })

df.to_csv('j7.csv',index=False)
