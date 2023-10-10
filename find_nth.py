import numpy as np 
def find_nth(data, n):
# your code goes here 
       flat = data.flatten()
       b = np.sort(flat)
       return b[b.size-n], b[n-1]
a = np.array([ 
       [0.8147, 0.0975, 0.1576], 
       [0.9058, 0.2785, 0.9706], 
       [0.127 , 0.5469, 0.9572], 
       [0.9134, 0.9575, 0.4854], 
       [0.6324, 0.9649, 0.8003]]) 
print(find_nth(a, 1)) 
print(find_nth(a, 2)) 
print(find_nth(a, 3))