from typing import List, Dict
import numpy as np


class FillLevelEstimator:
    def estimate(self, frame: np.ndarray, detections: List[Dict]) -> float:
        # Placeholder: simple heuristic (no detections => low fill)
        return 10.0 if len(detections) == 0 else 60.0


