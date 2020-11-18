import pandas as pd

pybiomed_df = pd.read_csv('../datasets/trainingDatasets/pybiomed_generated_features.csv')
logisticRegression_df = pd.read_csv('../datasets/testResults/logisticRegression/logisticRegressionResults.csv')

logisticRegressionResults_df = logisticRegression_df[['prediction(CLASS)']].copy()
pybiomed_df_sequences = pybiomed_df[['Sequence']].copy()

concatLogisticRegressionResults_df = pd.concat([pybiomed_df_sequences, logisticRegressionResults_df], axis=1)

print(concatLogisticRegressionResults_df)

concatLogisticRegressionResults_df.to_csv('../datasets/testResults/logisticRegression/logisticRegressionResultsAppended')