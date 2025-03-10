import pandas as pd

df = pd.read_json('News_Category_Dataset_v3.csv', lines=True)

print(df)

row_count = len(df)
print(row_count)

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

duplicates = df.duplicated()
print("Duplicate rows")
print(df[duplicates])

#duplicates = df.duplicated()
#print("Duplicate rows")
#print(duplicates)

print(duplicates.sum())


df_cleaned = df.drop_duplicates()
print("DataFrame without duplicates")
print(df_cleaned)

print(duplicates.sum())

df_cleaned.to_csv('News_Category_Dataset_v3.csv', index=False)