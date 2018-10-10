import numpy as np
def is_prime(a):
    r=a%np.arange(2,a)
    return np.all(r!=0)
def search():
    counter=1;record=(None,None)
    for i in range(1000,1000000):
        if is_prime(i):
            if is_prime(i+2):
                record=(i,i+2)
                counter+=1
                print('{}:\t{}'.format(counter,record))
                
search()