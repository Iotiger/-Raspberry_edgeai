import numpy as np
from edge.fill_level.estimator import FillLevelEstimator


def test_fill_level_heuristic():
    estimator = FillLevelEstimator()
    frame = np.zeros((10, 10, 3), dtype=np.uint8)
    empty = estimator.estimate(frame, [])
    assert 0.0 <= empty <= 100.0
    some = estimator.estimate(frame, [{"label": "plastic", "confidence": 0.9, "bbox": [0,0,1,1]}])
    assert some >= empty



# tweak 9 at 2025-09-24 20:37:39

# tweak 28 at 2025-09-24 20:37:47
