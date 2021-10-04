import pandas as pd
df=pd.DataFrame({ "name":[ 'yash','akash','dhruvi','meet','savan','dhruvin','gd','maulik','ridhhi','axit'],
                "rollno":['101','102','103','104','105','106','107','108','109','110'],
                "city":['surat','ahemdabad','vadodra','bhavnagar','rajkot','ahemdabad','rajkot','bhavnagar','vadodra','surat']
        })
print('*************Top five Rows*************')
top5=df.head(5)
print(top5)

print('*************Last five Rows*************')
last5=df.tail(5)
print(last5)