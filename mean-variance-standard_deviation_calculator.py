import numpy as np

def calculate(list):

    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
  
    calculations = {}
    arr = np.array(list).reshape(3,3)
    mean = [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr)]
    variance = [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr)]
    std = [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr)]
    max = [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr)]
    min = [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr)]
    sum = [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr)]
    calculations["mean"] = mean
    calculations["variance"] = variance
    calculations["standard deviation"] = std
    calculations["max"] = max
    calculations["min"] = min
    calculations["sum"] = sum
    print(calculations)

    return calculations