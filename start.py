import re
import numpy as np
from collections import Counter
import scipy
from scipy.spatial.distance import cosine

c = 0
k = 0
t = 0
m = 0
i = 0
j = 0
lines = []
D = {}
Lwords = []
L = []
file_obj = open('sentences.txt', 'r')
for line1 in file_obj:
    line1 = line1.lower()
    dirty_file = re.split('[^a-z]', line1)
    Lwords = Lwords + dirty_file
    lines.append(line1)
    t+=1
clear_L = [x for x in Lwords if x]
for k in range(len(clear_L)):
    if clear_L[k] not in D:
        D[clear_L[k]] = k
    k+=1

file_obj = open('sentences.txt', 'r')
for line in file_obj:
    line = line.lower()
    line = re.split('[^a-z]', line)
    clear_line = [x for x in line if x]
    L.append(clear_line)

Matrix = np.zeros((len(L),len(D)), dtype=int)
np.set_printoptions(threshold=np.inf)

ListOfWords = list(D.keys())

for i in range(len(L)):
    line_counter = Counter(L[i])
    for j in range(len(D)):
        Matrix[i, j] = line_counter[ListOfWords[j]]

    m+=1

for c in range(len(L)):
    print(c, round((scipy.spatial.distance.cosine(Matrix[0], Matrix[c])),2))
    c+=1


