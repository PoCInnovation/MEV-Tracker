import numpy as np
import math

def sigmoid_math(x):
    """
    Arguments:
    x -- un nombre scalaire

    Return:
    s -- sigmoid_math(x)
    """

    ### Début du code ### (≈ 1 ligne de code)
    s = 1 / (1 + np.exp(-x))
    ### Fin du code ###

    return s

def sigmoid_deriv(x):
    """
    Arguments:
    x -- un nombre scalaire ou un numpy array

    Return:
    ds -- votre gradient
    """

    ### Début du code ### (≈ 2 lignes de code)
    s = sigmoid_math(x)
    ds = s * (1 - s)
    ### Fin du code ###

    return ds

def image_to_vector(image):
    """
    Argument:
    image -- un numpy array de shape (longueur, largeur, profondeur)
    
    Returns:
    v -- un vecteur de shape (longueur*largeur*profondeur, 1)
    """
    
    ### Début du code ### (≈ 1 ligne de code)
    print(image.shape)
    v = image.reshape((image.shape[0] * image.shape[1] * 2, 1))
    ### Fin du code ###

    return v

def normalize_rows(x):
    """
    Argument:
    x -- une matrice numpy x de shape (n, m)
    
    Returns:
    x -- la matrice normalisée x
    """
    
    ### Début du code ### (≈ 2 lignes de code)
    # Calculez d'abord la norme de x. Utilisez np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, ord = 2, axis = 1, keepdims = True)
    
    # Divisez x par x_norm.
    x = x / x_norm
    ### Fin du code ###

    return x

def softmax(x):
    """
    Argument:
    x -- Un vecteur ou une matrice numpy de shape (n,m)

    Returns:
    s -- Une matrice numpy égale au softmax de x, de shape (n,m)
    """
    
    ### Début du code ### (≈ 3 lignes de code)
    # Calculez l'exponentielle de chaque élément de x. Utilisez np.exp()
    x_exp = np.exp(x)

    # Créez un vecteur x_sum qui fait la somme de chaque ligne de x_exp. Utilisez np.sum(..., axis = 1, keepdims = True)
    x_sum = np.sum(x_exp, axis = 1, keepdims = True)
    
    # Calculer softmax(x) en divisant x_exp par x_sum. Cela utilisera automatiquement le broadcasting de numpy.
    s = x_exp / x_sum
    ### Fin du code ###
    print(x_exp.shape, x_sum.shape, s.shape)
    
    return s

def L1_function(y_predicted, y):
    """
    Arguments:
    y_predicted -- vecteur de size m contenant vos valeurs prédites
    y -- vecteur de size m contenant les vraies valeurs

    Returns:
    L1 -- valeur de la fonction de loss L1
    """

    ### Début du code ### (≈ 1 ligne de code)
    L1 = np.sum(np.abs(y_predicted - y))
    ### Fin du code ###

    return L1

def L2_function(y_predicted, y):
    ### Début du code ### (≈ 1 ligne de code)
    L2 = np.dot(y_predicted - y, y_predicted - y)
    ### Fin du coee ###
    
    return L2

# if __name__ == '__main__':
#     # x = np.array([1.5, 2.5, 3.5])
#     # print ("sigmoid_deriv(x) = " + str(sigmoid_deriv(x)))
#     # image = np.array([[[ 0.67126139,  0.29381281],
#     #     [ 0.90714982,  0.52835547],
#     #     [ 0.42245251 ,  0.45012151]],

#     #    [[ 0.92814219,  0.96677647],
#     #     [ 0.85114703,  0.52351845],
#     #     [ 0.19981397,  0.27417313]],

#     #    [[ 0.6213595,  0.00531265],
#     #     [ 0.1210313,  0.49974237],
#     #     [ 0.3432129,  0.94631277]]])
#     # print ("image_to_vector(image) = " + str(image_to_vector(image)))
#     # x = np.array([
#     # [2, 3, 6],
#     # [5, 2, 8]])
#     # print("normalize_rows(x) = " + str(normalize_rows(x)))
#     x_vect = np.array([[9, 4, 0, 0 ,0]]) #sisi 94 RPZ

#     print("softmax(x_vect) = " + str(softmax(x_vect)))

#     x_matr = np.array([
#         [1, 7, 5, 0, 6],
#         [3, 4, 0, 2 ,0]])

#     print("softmax(x_matr) = " + str(softmax(x_matr)))
    # y_predicted = np.array([.8, 0.3, 0.2, .6, .2])
    # y = np.array([1, 1, 0, 1, 0])
    # print("L1 = " + str(L1_function(y_predicted,y)))
    y_predicted = np.array([.8, 0.3, 0.2, .6, .2])
    y = np.array([1, 1, 0, 1, 0])
    print("L2 = " + str(L2_function(y_predicted,y)))