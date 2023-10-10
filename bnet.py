import sys

class bnet:
    p_b = .001
    p_e = .002
    p_a = [[.95, .94], [.29, .001]]
    p_j = [.9, .05]
    p_m = [.7, .01]
    B=None
    E=None
    A=None
    J=None
    M=None
    
    def __init__(self):
        pass
    
    def computeProbability(self, b, e, a, j, m):
        x=1
        if b:
            x=0
        y=1
        if e:
            y=0
        z=1
        if a:
            z=0
        probability = 1
        if b:
            probability *= self.p_b
        else:
            probability *= 1-self.p_b
        if e:
            probability *= self.p_e
        else:
            probability *= 1-self.p_e
        if a:
            probability *= self.p_a[x][y]
        else:
            probability *= 1-self.p_a[x][y]
        if j:
            probability *= self.p_j[z]
        else:
            probability *= 1-self.p_j[z]
        if m:
            probability *= self.p_m[z]
        else:
            probability *= 1-self.p_m[z]
        
        
            
        return probability
    
    def getReady(self, b, e, a, j, m):
        if b == None:
            return self.getReady(b=True, e=e, a=a, j=j, m=m) + self.getReady(b=False, e=e, a=a, j=j, m=m)
        elif e == None:
            return self.getReady(b=b, e=True, a=a, j=j, m=m) + self.getReady(b=b, e=False, a=a, j=j, m=m)
        elif a == None:
            return self.getReady(b=b, e=e, a=True, j=j, m=m) + self.getReady(b=b, e=e, a=False, j=j, m=m)
        elif j == None:
            return self.getReady(b=b, e=e, a=a, j=True, m=m) + self.getReady(b=b, e=e, a=a, j=False, m=m)
        elif m == None:
            return self.getReady(b=b, e=e, a=a, j=j, m=True) + self.getReady(b=b, e=e, a=a, j=j, m=False)
        else:
            return self.computeProbability(b, e, a, j, m)
        
        

flip = False

left_side = []
right_side = []
        
for i in range(1, len(sys.argv)):
    if sys.argv[i] == 'given':
        flip = True
        continue
    if flip:
        right_side.append((sys.argv[i][0], sys.argv[i][1]))
    else:
        left_side.append((sys.argv[i][0], sys.argv[i][1]))

values = left_side+right_side
network = bnet()

numerator = 0
denominator = 0

for i in right_side:
    if i[1] == 'f':
        if i[0] == 'B':
            network.B = False
            continue
        if i[0] == 'E':
            network.E = False
            continue
        if i[0] == 'A':
            network.A = False
            continue
        if i[0] == 'J':
            network.J = False
            continue
        if i[0] == 'M':
            network.M = False
            continue
    else:
        if i[0] == 'B':
            network.B = True
            continue
        if i[0] == 'E':
            network.E = True
            continue
        if i[0] == 'A':
            network.A = True
            continue
        if i[0] == 'J':
            network.J = True
            continue
        if i[0] == 'M':
            network.M = True
            continue

if len(right_side) > 0:
    denominator = network.getReady(network.B, network.E, network.A, network.J, network.M)

for i in values:
    if i[1] == 'f':
        if i[0] == 'B':
            network.B = False
            continue
        if i[0] == 'E':
            network.E = False
            continue
        if i[0] == 'A':
            network.A = False
            continue
        if i[0] == 'J':
            network.J = False
            continue
        if i[0] == 'M':
            network.M = False
            continue
    else:
        if i[0] == 'B':
            network.B = True
            continue
        if i[0] == 'E':
            network.E = True
            continue
        if i[0] == 'A':
            network.A = True
            continue
        if i[0] == 'J':
            network.J = True
            continue
        if i[0] == 'M':
            network.M = True
            continue
    
numerator = network.getReady(network.B, network.E, network.A, network.J, network.M)

if len(right_side) > 0:
    print("Probability = %.5f" % (numerator/denominator))
else:
    print("Probability = %.5f" % (numerator))