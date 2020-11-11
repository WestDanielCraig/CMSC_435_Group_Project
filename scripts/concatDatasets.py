import pandas as pd

aac_df = pd.read_csv('../datasets/final_amino_acid_result.csv')
bioP_df = pd.read_csv('../datasets/training_data.csv', index_col=0)

aac_df_no_id = aac_df.drop(columns=['ID'])
bioP_df_drop = bioP_df.drop(columns=['PROTEIN SEQUENCE', 'Length', 'Instability Index', 'COUNT-A', 'COUNT-C', 'COUNT-D',
                                     'COUNT-E', 'COUNT-F', 'COUNT-G', 'COUNT-H', 'COUNT-I', 'COUNT-K',
                                     'COUNT-L', 'COUNT-M', 'COUNT-N', 'COUNT-P', 'COUNT-Q', 'COUNT-R',
                                     'COUNT-S', 'COUNT-T', 'COUNT-V', 'COUNT-W', 'COUNT-Y', 'Cysteines Reduced', 'Cystines Residues'])

print(aac_df_no_id)
print(bioP_df_drop)

concat_dataset = pd.concat([bioP_df_drop, aac_df_no_id], axis=1)

print(concat_dataset)

concat_dataset.to_csv('../datasets/concat_dataset.csv', index=False)

