import pandas as pd

pybiomed_df = pd.read_csv('../datasets/testDatasets/generated_features_test.csv')
bioP_df = pd.read_csv('../datasets/testDatasets/testing_data.csv', index_col=0)
physico_chemical_df = pd.read_csv('../datasets/testDatasets/test_physico-chemical_result.csv')
combined_csv_df = pd.read_csv('../datasets/testDatasets/test_combined_csv.csv')
dipeptide_training_df = pd.read_csv('../datasets/testDatasets/dipeptide_test.csv')
final_amphiphilic_pseudo_result_df = pd.read_csv('../datasets/testDatasets/test_amphiphilic_pseudo_result.csv')
final_pseudo_result_df = pd.read_csv('../datasets/testDatasets/test_pseudo_result.csv')
final_quasi_result_df = pd.read_csv('../datasets/testDatasets/test_quasi_result.csv')



pybiomed_df_drop = pybiomed_df.drop(columns=['Sequence'])
bioP_df_drop = bioP_df.drop(columns=['PROTEIN SEQUENCE', 'Length', 'Instability Index', 'COUNT-A', 'COUNT-C', 'COUNT-D',
                                     'COUNT-E', 'COUNT-F', 'COUNT-G', 'COUNT-H', 'COUNT-I', 'COUNT-K',
                                     'COUNT-L', 'COUNT-M', 'COUNT-N', 'COUNT-P', 'COUNT-Q', 'COUNT-R',
                                     'COUNT-S', 'COUNT-T', 'COUNT-V', 'COUNT-W', 'COUNT-Y', 'Cysteines Reduced',
                                     'Cystines Residues'])
physico_chemical_df_drop = physico_chemical_df.drop(columns=['ID'])
combined_csv_df_drop = combined_csv_df.drop(columns=['Sequence_identifier'])
dipeptide_training_df_drop = dipeptide_training_df.drop(columns=['Sequence_identifier'])
final_amphiphilic_pseudo_result_df_drop = final_amphiphilic_pseudo_result_df.drop(columns=['ID'])
final_pseudo_result_df_drop = final_pseudo_result_df.drop(columns=['ID'])
final_quasi_result_df_drop = final_quasi_result_df.drop(columns=['ID'])

#print(aac_df_drop)
print(pybiomed_df_drop)
#print(physico_chemical_df_drop)
#print(bioP_df_drop)
#print(combined_csv_df_drop)
#print(dipeptide_training_df_drop)
#print(final_amphiphilic_pseudo_result_df_drop)
#print(final_pseudo_result_df_drop)
#print(final_quasi_result_df_drop)

concat_dataset_test = pd.concat([bioP_df_drop, pybiomed_df_drop, physico_chemical_df_drop, combined_csv_df_drop,
                            dipeptide_training_df_drop, final_amphiphilic_pseudo_result_df_drop,
                            final_pseudo_result_df_drop, final_quasi_result_df_drop], axis=1)

print(concat_dataset_test)

concat_dataset_test.to_csv('../datasets/testDatasets/concat_dataset_test.csv', index=False)

