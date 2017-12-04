import numpy as np
import pandas as pd
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:-0.6922854322689991
exported_pipeline = make_pipeline(
    RBFSampler(gamma=0.8),
    LogisticRegression(C=0.01, dual=False, penalty="l1")
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)