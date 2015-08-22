__author__ = 'brett'
from collections.abc import MutableMapping


class Chart(MutableMapping):
    def __init__(self, **kwargs):
        self._internal = {
            'element_id': 'chart',
            'chart_type': 'Line',
            'width': '400',
            'height': '400',
            'data': {
                'labels': ["January", "February", "March", "April", "May", "June", "July"],
                'datasets': [
                    {
                        'label': "My First dataset",
                        'fillColor': "rgba(220,220,220,0.2)",
                        'strokeColor': "rgba(220,220,220,1)",
                        'pointColor': "rgba(220,220,220,1)",
                        'pointStrokeColor': "#fff",
                        'pointHighlightFill': "#fff",
                        'pointHighlightStroke': "rgba(220,220,220,1)",
                        'data': [65, 59, 80, 81, 56, 55, 40]
                    },
                    {
                        'label': "My Second dataset",
                        'fillColor': "rgba(151,187,205,0.2)",
                        'strokeColor': "rgba(151,187,205,1)",
                        'pointColor': "rgba(151,187,205,1)",
                        'pointStrokeColor': "#fff",
                        'pointHighlightFill': "#fff",
                        'pointHighlightStroke': "rgba(151,187,205,1)",
                        'data': [28, 48, 40, 19, 86, 27, 90]
                    }
                ]
            },
            'options': {}
        }
        self._internal.update(kwargs)

    def __getitem__(self, item):
        return self._internal.__getitem__(item)

    def __setitem__(self, key, value):
        self._internal.__setitem__(key, value)

    def __delitem__(self, key):
        self._internal.__delitem__(key)

    def __iter__(self):
        return self._internal.__iter__()

    def __len__(self):
        return self._internal.__len__()
