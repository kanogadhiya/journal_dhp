import csv

csv_file='j6.csv'
with open (csv_file,'w') as j:
    keys=['name','rollno','city']
    writer = csv.writer(j)
    writer.writerow(keys)
    writer.writerow({ "name":'yash', "rollno":101,"city":'surat'}.values())
    writer.writerow({ "name":'akash', "rollno":102,"city":'ahemdabad'}.values())
    writer.writerow({ "name":'dhruvi', "rollno":103,"city":'vadodra'}.values())
    writer.writerow({ "name":'meet', "rollno":104,"city":'bhavnagar'}.values())
    writer.writerow({ "name":'savan', "rollno":105,"city":'rajkot'}.values())



# import csv
# import pandas as pd
# dic={    "name":['yash','akash','dhruvi','meet','savan'],
#     "rollno":['101','102','103','104','105'],
#     "city":['surat','ahemdabad','vadodra','bhavnagar','rajkot'] 
# }
# df=pd.DataFrame(dic,columns=["name","rollno","city"])
# print(df)
# df.to_csv('j6.csv',index=False)
