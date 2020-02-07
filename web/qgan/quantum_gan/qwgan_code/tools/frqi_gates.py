from .qcircuit import *

# 量子状態の状態ベクトルを取得
    
    
def C2RY_00(size, control1, control2, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    return matrix
    
    
def C2RY_10(size, control1, control2, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    return matrix
    
    
def C2RY_01(size, control1, control2, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    return matrix
    
    
def C2RY_11(size, control1, control2, target, param):
    matrix = Identity(size)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCNOT(size, control1, control2, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    return matrix

    
    
def C4RY_0000(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix
    
    
def C4RY_1000(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix

  
  
def C4RY_0100(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix
    
    
    
def C4RY_0010(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix
    
    
def C4RY_0001(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    return matrix
    
    
    
def C4RY_1100(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix  
    
    
def C4RY_1010(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix 
    
    
    
def C4RY_1001(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    return matrix
    
    
def C4RY_0110(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix
    
    
def C4RY_0101(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    return matrix 
    
    
def C4RY_0011(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    return matrix
    
    
def C4RY_1110(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control4), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control4), matrix)
    return matrix
    
    
def C4RY_1101(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control3), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control3), matrix)
    return matrix  
    
    
def C4RY_1011(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control2), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control2), matrix)
    return matrix
    

def C4RY_0111(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(X(size,control1), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    matrix = np.matmul(X(size,control1), matrix)
    return matrix
    
    
def C4RY_1111(size, control1, control2, control3, control4, target, param):
    matrix = Identity(size)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, -param/2, False), matrix)
    matrix = np.matmul(CCCCNOT(size, control1, control2, control3, control4, target), matrix)
    matrix = np.matmul(RY(size, target, param/2, False), matrix)
    return matrix    
     
  