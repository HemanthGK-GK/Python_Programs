# Write a Python program to convert a Panda module Series to Python list and it's type.
import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Converting Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))
