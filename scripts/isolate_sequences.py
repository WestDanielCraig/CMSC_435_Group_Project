import pandas as pd

# This script strips the classifications from sequence_training.txt
 
df = pd.read_csv('../datasets/sequences_training(3).txt')
second_column = df.columns[1]
df = df.drop([second_column], axis=1)
df.to_csv('../datasets/just_sequences.txt', index=False)

print(df)