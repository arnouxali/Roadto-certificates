import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    inp = np.reshape(list, (3, 3))
    stats_dict = {
        'mean': [
            np.mean(inp, axis=0).tolist(),
            np.mean(inp, axis=1).tolist(),
            np.mean(inp).item()
        ],
        'variance': [
            np.var(inp, axis=0).tolist(),
            np.var(inp, axis=1).tolist(),
            np.var(inp).item()
        ],
        'standard deviation': [
            np.std(inp, axis=0).tolist(),
            np.std(inp, axis=1).tolist(),
            np.std(inp).item()
        ],
        'max': [
            np.max(inp, axis=0).tolist(),
            np.max(inp, axis=1).tolist(),
            np.max(inp).item()
        ],
        'min': [
            np.min(inp, axis=0).tolist(),
            np.min(inp, axis=1).tolist(),
            np.min(inp).item()
        ],
        'sum': [
            np.sum(inp, axis=0).tolist(),
            np.sum(inp, axis=1).tolist(),
            np.sum(inp).item()
        ]

    }



    return stats_dict