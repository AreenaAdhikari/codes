import pandas as pd
import numpy as np
student_data = {'name':['Ansia','Kartia','Nili','Nilu','sixro','sixto','sito','Anara','Anra','akirta'],
               'grade' : [4,5,6,7,8,8,2,9,7,8],
               'AGE': [4,10,11,12,13,14,15,15,4,16],
               'class section' : ['1-a','2-b','3-c','4f','N5','N6','7-a','9-10a','N9-14','ND-k4'] }
Labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(student_data, index=Labels)
print("This is the summary of all the data in this data frame: :) : ")
print(df.info())