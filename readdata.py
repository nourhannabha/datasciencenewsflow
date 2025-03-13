import pandas as pd

df = pd.read_csv('News_Category_Dataset_v3.csv')

print(df)

row_count = len(df)
print(row_count)

print(df.head())

print(df.info())

print(df.describe())

print(df.dtypes)

print(df.isnull().sum())

duplicates = df.duplicated()
print("Duplicate rows")
print(df[duplicates])

#duplicates = df.duplicated()
#print("Duplicate rows")
#print(duplicates)

print(duplicates.sum())

df_cleaned = df.drop_duplicates().dropna()

print("DataFrame without duplicates and missing values")
print(df_cleaned)

print("Missing values after cleaning:")
print(df_cleaned.isnull().sum())

print("Duplicate rows after cleaning:")
print(df_cleaned.duplicated().sum())

print("Original shape:", df.shape)
print("New shape after cleaning:", df_cleaned.shape)

df_cleaned.to_csv('News_Category_Dataset_v3.csv', index=False)
