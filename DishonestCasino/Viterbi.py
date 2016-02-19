from Die import FairDie
from Die import LoadedDie

class Viterbi(object):
    """ Viterbi algorithm """
    
    # Decoding algorithm
    def Decode(self, sequence):
        n = len(sequence)
        matrix = []
        matrix.append([0] * n)
        matrix.append([0] * n)

        # Filling the matrix with probabilities 
        matrix[0][0] = FairDie.probabiltyOfRolling(float(sequence[0])) * 0.5
        matrix[1][0] = LoadedDie.probabiltyOfRolling(float(sequence[0])) * 0.5
        for i in range(1, n):
            matrix[0][i] = FairDie.probabiltyOfRolling(float(sequence[i])) * max(matrix[0][i - 1] * (1 - FairDie.switchProability), matrix[1][i - 1] * LoadedDie.switchProability)
            matrix[1][i] = LoadedDie.probabiltyOfRolling(float(sequence[i])) * max(matrix[0][i - 1] * FairDie.switchProability, matrix[1][i - 1] * (1 - LoadedDie.switchProability))

        # print(matrix[0])
        # print(matrix[1])

        # Backtracking the solution
        # Find the highest probability and follow back the path with keeping the probability highest
        path = ""
        n -= 1
        while n > -1:
            if matrix[0][n] > matrix[1][n]:
                path += 'F'
            else:
                path += 'L'
            n -= 1

        return path[::-1]
