


# modules used in the function below
from math import *
from decimal import Decimal


"""
Similarity methods :: distance evaluation between two vectors, 
larger distance == very dis-similar objects
smaller distance == very similar objects.

"""



# 1.) Euclidean Distance (L2 norm)

'''
when data is dense or continous, simply the length of path connecting them

'''

def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
 



# 2.) Manhattan Distance (L1 norm)

'''
it is simply the sum of absolute dufferences of their cartesian coordinates

between two points (x1, y1) and (x2, y2)
manhattan distance = |x1 – x2| + |y1 – y2|

'''

def manhattan_distance(x, y):
    return sum(abs(a-b) for (a, b) in zip(x, y))


# 3.) Minkowski Distance 

'''

minkowski distance is the generalized form of euclideand and manhattan distance
lambda is the order of the minkowski metric

when lamda = 1, it is manhattan distance
when lamda = 2, it is euclidean distance

'''

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)
 
def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)



# 4.) Cosine similarity

'''
particulary used in positive space
easy to compute for sparse vectors
'''

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)


# 5.) Jaccard Similarity

'''

cardinality of set A =  |A| = how many elements are there in A
intersection of A and B = all items common in both A and B
union of A and B = all items which are in either set.


so, jacard(a, b) = |intersection(a, b)| / |union(a, b)|

'''

def jaccard_similarity(x,y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)




a = [1, 2, 3]
b = [2, 3, 4]


