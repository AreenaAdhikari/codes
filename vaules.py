import pandas as pd
import numpy as np
exam_data = {'name':['Anastaia', 'Kevin','Jake', 'Michael','san', 'stan', 'kiara','Nina','kiro','Snape'],
            'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,10,10],
            'attemps': [1,3,2,3,2,3,1,1,2,1],
            'grade' : ['yes','no','yes','no','no','yes','yes','no','no','yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data, index=labels)
print("Sumarry of the info in this data frame:")
print(df.info())
