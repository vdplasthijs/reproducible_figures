import datetime

import pytest


@pytest.fixture(scope='session')
def figure_layout1_fixture():
    layout = {'A': {'panel_shape': (1, 1,'twinx'), 'bound': (0.15, 0.75, 0.45, 0.90)}, 'A"': {'panel_shape': (1, 2), 'bound': (0.15, 0.60, 0.45, 0.90), 'hspace': 0.6}, 'B': {'panel_shape': (1, 1), 'bound': (0.6, 0.75, 0.67, 0.90)}}

    return layout