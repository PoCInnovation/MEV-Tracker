import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from lr_utils import load_dataset

x_train_orig, y_train, x_test_orig, y_test, classes = load_dataset()
# index = 30
# plt.imshow(x_train_orig[index])
# if classes[np.squeeze(y_train[:, index])] == b'cat':
#     print("y = " + str(y_train[:, index]) + ", ceci est une photo de chat")
# else:
#     print("y = " + str(y_train[:, index]) + ", ceci n'est pas une photo de chat")

# ### Début du code ### (≈ 3 lignes de code)
# m_train = x_train_orig.shape[0]
# m_test = x_test_orig.shape[0]
# num_px = x_train_orig.shape[1]
# ### Fin du code ###

# print ("Nombre d'exemples de train: m_train = " + str(m_train))
# print ("Nombre d'exemples de test: m_test = " + str(m_test))
# print ("Longueur/Largeur de chaque image: num_px = " + str(num_px))
# print ("Chaque image est de size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
# print ("x_train shape: " + str(x_train_orig.shape))
# print ("y_train shape: " + str(y_train.shape))
# print ("x_test shape: " + str(x_test_orig.shape))
# print ("y_test shape: " + str(y_test.shape))


### Début du code ### (≈ 2 lignes de code)
x_train_flatten = None
x_test_flatten = None
### Fin du code ###

print ("x_train_flatten shape: " + str(x_train_flatten.shape))
print ("y_train shape: " + str(y_train.shape))
print ("x_test_flatten shape: " + str(x_test_flatten.shape))
print ("y_test shape: " + str(y_test.shape))
print ("check 1 random après reshaping: " + str(x_train_flatten[5:10,1]))
print ("check 2 random après reshaping: " + str(x_train_flatten[17:22,34]))