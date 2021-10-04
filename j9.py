import pandas as pd
dataf1=pd.DataFrame({ "name":[ 'yash','akash','dhruvi','meet','savan'],
            "rollno":['101','102','103','104','105']})
dataf2=pd.DataFrame({ "name":[ 'yash','akash','dhruvi','meet','savan'],
            "rollno":['101','102','103','104','105'],
            "city":['surat','ahemdabad','vadodra','bhavnagar','rajkot']})
# print(dataf1)
# print(dataf2)
with pd.ExcelWriter("excle_writer.xlsx") as writer:
    dataf1.to_excel(writer,index=False,sheet_name='sheet1')
    dataf2.to_excel(writer,index=False,sheet_name='sheet2')