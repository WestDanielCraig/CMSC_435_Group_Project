import pandas as pd

sequences_test_df = pd.read_csv('../datasets/sequences_test.csv')
logisticRegression_df = pd.read_csv('../datasets/testResults/logisticRegression/logisticRegressionResults.csv')

sequences_test_df.columns =['Sequence']

logisticRegressionResults_df = logisticRegression_df[['prediction(CLASS)']].copy()

concatLogisticRegressionResults_df = pd.concat([sequences_test_df, logisticRegressionResults_df], axis=1)

print(concatLogisticRegressionResults_df)

concatLogisticRegressionResults_df.to_csv('../datasets/testResults/logisticRegression/logisticRegressionResultsAppended.txt', index=0, header=0)

logisticRegressionResults_df.to_csv('../datasets/testResults/logisticRegression/logisticRegressionResultsProteinOnly.txt', index=0, header=0)

