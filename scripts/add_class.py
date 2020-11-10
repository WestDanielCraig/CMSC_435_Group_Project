import pandas as pd

# This script takes the features csv and appends the classifcations from sequence_training

df1 = pd.read_csv('../datasets/final_amino_acid_result.csv', header=0)
df2 = pd.read_csv('../datasets/sequences_training(3).txt', header=None)
df2.columns = ['Sequence', 'Class']


for row in df1.iterrows():
    df1['Class'] = df2.iloc[:,1]

df1.to_csv('../datasets/features_plus_classes.csv', index=False)
# df2.to_csv('original_training.csv', index=False)
