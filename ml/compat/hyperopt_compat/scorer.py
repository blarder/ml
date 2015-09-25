from sklearn.base import clone
from sklearn.cross_validation import cross_val_score
from hyperopt import STATUS_OK


class CrossValScorer(object):

    def __init__(self, data, target, estimator, coerce_to_int=()):
        self.data = data
        self.target = target
        self.coerce_to_int = coerce_to_int
        self.estimator = estimator

    def __call__(self, param_dict):
        for key in self.coerce_to_int:
            if key in param_dict:
                param_dict[key] = int(param_dict[key])
        new_estimator = clone(self.estimator)

        new_estimator.set_params(**param_dict)

        score = cross_val_score(new_estimator, self.data, self.target)

        return {
            'loss': - sum(score) / len(score),
            'status': STATUS_OK,
            'params': param_dict
        }
