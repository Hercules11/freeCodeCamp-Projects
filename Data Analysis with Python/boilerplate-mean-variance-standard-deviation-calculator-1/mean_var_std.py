import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    # assert len(list) == 9, "List must contain nine numbers."
    a = np.array(list).reshape(3, 3)
    result = {}
    mean = [np.mean(a, axis=0).tolist(), np.mean(a, axis=1).tolist(), np.mean(a)]
    result["mean"] = mean

    variance = [np.var(a, axis=0).tolist(), np.var(a, axis=1).tolist(), np.var(a)]
    result["variance"] = variance

    std_dev = [np.std(a, axis=0).tolist(), np.std(a, axis=1).tolist(), np.std(a)]
    result["standard deviation"] = std_dev

    max_val = [np.max(a, axis=0).tolist(), np.max(a, axis=1).tolist(), np.max(a)]
    result["max"] = max_val

    min_val = [np.min(a, axis=0).tolist(), np.min(a, axis=1).tolist(), np.min(a)]
    result["min"] = min_val

    sum_val = [np.sum(a, axis=0).tolist(), np.sum(a, axis=1).tolist(), np.sum(a)]
    result["sum"] = sum_val
    return result


# print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))


# https://www.jianshu.com/p/f4e9407f9f9d
