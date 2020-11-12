import pandas as pd

aac_df = pd.read_csv('../datasets/final_amino_acid_result.csv')
pybiomed_df = pd.read_csv('../datasets/pybiomed_generated_features.csv')
bioP_df = pd.read_csv('../datasets/training_data.csv', index_col=0)
physico_chemical_df = pd.read_csv('../datasets/final_physico_chemical_result.csv')


aac_df_no_id = aac_df.drop(columns=['ID'])
pybiomed_df_drop = pybiomed_df.drop(columns=['Sequence', 'Label'])
bioP_df_drop = bioP_df.drop(columns=['PROTEIN SEQUENCE', 'Length', 'Instability Index', 'COUNT-A', 'COUNT-C', 'COUNT-D',
                                     'COUNT-E', 'COUNT-F', 'COUNT-G', 'COUNT-H', 'COUNT-I', 'COUNT-K',
                                     'COUNT-L', 'COUNT-M', 'COUNT-N', 'COUNT-P', 'COUNT-Q', 'COUNT-R',
                                     'COUNT-S', 'COUNT-T', 'COUNT-V', 'COUNT-W', 'COUNT-Y', 'Cysteines Reduced',
                                     'Cystines Residues'])
physico_chemical_df_drop = physico_chemical_df.drop(columns=["ID"])

#print(aac_df_no_id)
#print(pybiomed_df_drop)
print(physico_chemical_df_drop)
#print(bioP_df_drop)

concat_dataset = pd.concat([bioP_df_drop, pybiomed_df_drop, physico_chemical_df_drop], axis=1)
# concat_dataset = pd.concat([bioP_df_drop, pybiomed_df_drop, aac_df_no_id], axis=1)

#print(concat_dataset)

concat_dataset.to_csv('../datasets/concat_dataset.csv', index=False)

