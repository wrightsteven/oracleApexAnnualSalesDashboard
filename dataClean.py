import pandas as pd

df = pd.read_csv("/Users/steven/Desktop/annual_data_2019_copy.csv")

#Drop null values
df = df[df['Order Date'].str[0:2] != 'Or']
df.dropna(how='any',inplace=True)

#Assign correct data types to columns
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

#Add month column
df['Month'] = df['Order Date'].str[0:2]
df['Month'] = df['Month'].astype('int32')

#Add city column
def getCity(address):
    return address.split(",")[1].strip(" ")

def getState(address):
    return address.split(",")[2].split(" ")[1]

df['City'] = df['Purchase Address'].apply(lambda x: getCity(x) + ' ' + getState(x))

#Add sales column
df['Sales'] = df['Quantity Ordered'].astype('int') * df['Price Each'].astype('float')

#Add hour, minute, and count columns
df['Hour'] = pd.to_datetime(df['Order Date']).dt.hour
df['Minute'] = pd.to_datetime(df['Order Date']).dt.minute
df['Count'] = 1



df.to_csv("/Users/steven/Desktop/annual_data_2019_clean.csv")
