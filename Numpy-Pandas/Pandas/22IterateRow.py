#Write a Python program to iterate over rows in a DataFrame
import pandas as pd
exam_data = [{'name':'Manu', 'score':10.5},
             {'name':'Deepa','score':8.9},
             {'name':'Manju','score':15.5}]
df = pd.DataFrame(exam_data)
for index, row in df.iterrows():
    print(row['name'], row['score'])
