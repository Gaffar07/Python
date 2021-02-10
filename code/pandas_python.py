import pandas as pd
from pandas import DataFrame

# di={'name':['gaffar','shaikh'],
#     'surname':['shaikh','ladale'],
#     'education':['msc','mba'],
#     'contact':['8850426734','8976125215']
# }
#
# x=pd.DataFrame(di)
# print(x)

#it is used for data analysis in python

#introduction pandas
#dataframe and series


# how to view data
# Selectinng data
# handling missing data
# pandas operation
# merge, group,reshape data
# time series and categorical
# plotting using pandas

import pandas as pd
import numpy as np

# s=pd.Series([1,2,3,4,5,np.NAN,6,7,8,9,10])
# print(s)

d=pd.date_range("20200301", periods=12)
#print(d)

df=pd.DataFrame(np.random.randn(12,4),index=d,columns=['A','B','C','D'])
print(df)

#df.head returns first five rows
#print(df.head())
#df.tail returns first five rows
#print(df.tail())

#df.index:returns theindex values
#df.columns :returnd the columns data
#df.tonumpy:returns the numpy array
#df.describe:returns the calculation part of data


#print(df.sort_index(axis=1,ascending=False)):sort from index values
#print(df.sort_values(by='C'))#:sort from values give columns name

#print(df['B'])#print single column vallues

#print the first two row
#print(df[0:3])

#print(df.loc[d[0]])
