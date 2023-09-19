import numpy as np

def calculate(list):
  if len(list) == 9:
    x = np.array(list).reshape(3, 3)
    calculations = {
      'mean' : [np.mean(x, axis=0).tolist(),
              np.mean(x, axis=1).tolist(),
              np.mean(x)],
      'variance' : [np.var(x, axis=0).tolist(),
                  np.var(x, axis=1).tolist(),
                  np.var(x)],
      'standard deviation' : [np.std(x, axis=0).tolist(),
                            np.std(x, axis=1).tolist(),
                            np.std(x)],
      'max' : [np.max(x, axis=0).tolist(),
              np.max(x, axis=1).tolist(),
              np.max(x)],
      'min' : [np.min(x, axis=0).tolist(),
              np.min(x, axis=1).tolist(),
              np.min(x)],
      'sum' : [np.sum(x, axis=0).tolist(),
              np.sum(x, axis=1).tolist(),
              np.sum(x)]
    }
  else:
    raise ValueError('List must contain nine numbers.')
  return calculations