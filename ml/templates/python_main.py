from __future__ import with_statement
import sys
import json

from sklearn.pipeline import make_pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn import datasets
from xgboost import XGBClassifier


model_output_file = sys.argv[1]
metadata_output_file = sys.argv[2]

# ALGORITHM GOES HERE! EXAMPLE -

iris = datasets.load_iris()
pipeline = make_pipeline(StandardScaler(), XGBClassifier())

param_grid = {
    'xgbclassifier__n_estimators': [50, 100, 200, 400],
    'xgbclassifier__learning_rate': [0.1, 0.05, 0.025]
}

grid_search_cv = GridSearchCV(pipeline, param_grid, n_jobs=-1)
grid_search_cv.fit(iris.data, iris.target)

# END EXAMPLE

joblib.dump(grid_search_cv, model_output_file)

with open(metadata_output_file, 'w') as f:
    f.write(str(grid_search_cv.grid_scores_))
