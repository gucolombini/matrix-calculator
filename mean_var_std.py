import numpy as np

def calculate(list):

    # Verificação se o input é uma lista de 9 números, retorna erro se não for o caso (obedecendo o teste)
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista numa array numpy
    array = np.array(list)
    
    # Cria uma matriz separando a lista em três linhas
    matrix = [array[[0, 1, 2]], array[[3, 4, 5]], array[[6, 7, 8]]]
    
    calculations = {
        'mean': [
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).tolist()
        ],
        'variance': [
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).tolist()
        ],
        'standard deviation': [
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).tolist()
        ],
        'max': [
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).tolist()
        ],
        'min': [
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).tolist()
        ],
        'sum': [
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).tolist()
        ]
    }
    
    return calculations
