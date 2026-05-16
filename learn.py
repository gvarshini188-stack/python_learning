
import pandas as pd 
import os
csv_path=os.path.join(os.path.dirname(__file__),'student_marks.csv')
df=pd.read_csv(csv_path)
#print(df)
#print(df.tail(3))
# print(df.shape)
# print(df.info())
#print(df.describe())
#print(df.columns())
# name_series=df['name']
# print(name_series)
# print(type(name_series))
# print(type(df))
# print(df.iloc[0])
# print(df.loc[0,'name'])
# print(df.iloc[0:3,1:3])
#filtering-example
# df_filtered=[df["Name"]=="eve davis"]
# print("students who scored>=50:",df_filtered)
# df_filtered=df[df["Score"]<50]
# print("students who scored<50:",df_filtered)
# top_science=df[(df['Subject']=='Science')& (df['Class']=="10A")]
# top_Math=df[(df['Subject']=='Science')& (df['Class']=="10A")]
# print(top_Math)
# print(top_science)
#Group by
# subject_avg=df.groupby('Subject')['Score'].mean()
# print(subject_avg)
# class_subject_avg=df.groupby(['Class','Subject'])
# print(class_subject_avg)
#aggregation
# stats=df.groupby('Subject')['Score'].agg(['mean','max','min','count'])
# print("stats:",stats)
#pivot_table
#pivot_table=df.pivot_table(index='Subject',columns='Class',values='Score',aggfunc='mean')
#print(pivot_table)
# df['Honors']=df['Score'].apply(lambda x: True if x>=90 else False)
# print(df[['Name',' Score','Honors']].head())
# january_sales=pd.DataFrame({"Item":["Apple","Banana"],"Sales":[100,150]})
# february_sales=pd.DataFrame({"Item":["Cherry","Dates"],"sales":[200,50]})
# print(january_sales)
# print(february_sales)
# employees=pd.DataFrame({"Emp_ID":[1,2,3],
#                         "Name":["John","Sarah","Mike"]})
# salaries=pd.DataFrame({"Emp_ID":[1,2,3],
#                        "Salary":[60000,80000,75000]})
# full_employee_data=pd.merge(employees,salaries,on="Emp_ID")
# print("Merged Employee Table:\n",full_employee_data)
