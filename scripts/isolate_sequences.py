import pandas as pd

# This script strips the classifications from sequence_training.txt
 
df = pd.read_csv('sequences_training(3).txt')
second_column = df.columns[1]
df = df.drop([second_column], axis=1)
df.to_csv('just_sequences.txt', index=False)

print(df)