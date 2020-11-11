import pandas as pd

aac_df = pd.read_csv('../datasets/final_amino_acid_result.csv')
bioP_df = pd.read_csv('../datasets/training_data.csv', index_col=0)

aac_df_no_id = aac_df.drop(columns=['ID'])

#print(aac_df_no_id)
#print(bioP_df)

concat_dataset = pd.concat([bioP_df, aac_df_no_id], axis=1)

#print(concat_dataset)

concat_dataset.to_csv('../datasets/concat_dataset.csv', index=False)

