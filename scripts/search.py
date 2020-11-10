import pandas as pd

# this script searches for the letters X,U,Z in each sequence and returns those rows

df = pd.read_csv('../datasets/original_training.csv')
df.columns = ['sequence','class']

# df2 = pd.DataFrame(columns = ['sequence','class','index'])
df2 = pd.DataFrame()

subX = 'X'
subU = 'U'
subZ = 'Z'

df['X'] = df['sequence'].str.find(subX)
df['U'] = df['sequence'].str.find(subU)
df['Z'] = df['sequence'].str.find(subZ)

# print(df)
cond = (df.X > 0) | (df.U > 0) | (df.Z > 0)
rows = df.loc[cond,:]
df2 = df2.append(rows, ignore_index=True)

df2 = df2.drop(df.columns[1], axis=1)
df2 = df2.drop(df.columns[2], axis=1)
df2 = df2.drop(df.columns[3], axis=1)
df2 = df2.drop(df.columns[4], axis=1)

print(df2)
# df2.to_csv('test2.csv', index=False)
df2.to_csv('../datasets/odd_sequences.csv', index=False)

# print(df)
# df.to_csv('test.csv', index=False)