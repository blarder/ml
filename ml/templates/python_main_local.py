from __future__ import with_statement, absolute_import

from sklearn.pipeline import make_pipeline
from sklearn import datasets
from hyperopt import fmin, tpe, hp
from hyperopt.mongoexp import MongoTrials

from hyperopt_compat.xgboost import XGBClassifier
from hyperopt_compat.scorer import CrossValScorer


# ALGORITHM GOES HERE! EXAMPLE -


iris = datasets.load_digits()
pipeline = make_pipeline(XGBClassifier(),)

search_space = {
    'xgbclassifier__n_estimators': hp.quniform('estimators', 3000, 10000, 1),
    'xgbclassifier__learning_rate': hp.uniform('learning_rate', 0.01, 0.1),
}

scorer = CrossValScorer(iris.data, iris.target, pipeline,
                        coerce_to_int=['xgbclassifier__n_estimators'])

trials = MongoTrials('mongo://localhost:27017/test_db/jobs', exp_key='exp1')
best = fmin(scorer,
            space=search_space,
            algo=tpe.suggest,
            max_evals=32,
            trials=trials)

print(trials.results)

print(best)
