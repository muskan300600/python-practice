import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
#['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename']
diabetes_X = diabetes.data[:,np.newaxis,2]
diabetes_X_train=diabetes_X[:-30]
diabetes_X_test = diabetes_X[-20:]

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-20:]



