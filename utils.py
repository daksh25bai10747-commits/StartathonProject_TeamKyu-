import numpy as np

CLASS_WEIGHTS = {
    0: 0.1,  # background
    1: 0.3,  # ground
    2: 0.8,  # rocks
    3: 0.6,  # trees
    4: 0.5,  # logs
    5: 0.4,  # bushes
    6: 0.2,  # grass
}

def compute_material_score(mask):
    total = 0
    for cls, w in CLASS_WEIGHTS.items():
        total += (mask == cls).sum() * w
    return total / mask.size