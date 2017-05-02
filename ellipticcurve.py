
"""函数式编程 
   
    def EllipticCurve(a,b):
    if(type(b) == list) :
    //执行初始化

    if(type(b) == int) :
    //执行函数

    //柯里化,Carrying


   

   EllipticCurve(F,L)

     y^2+L[0]xy+L[2]y modular P =x^3+L[1]x^2+L[3]x+L[4] modular P
    """

    """用对象重载__call()__使对象成为函数"""

    
class EllipticCurve:
    def __init__(self,F,L):
        self.F=F
        self.L=L
    def __call__(self,u,v):
        k = 3*x*x+2
        
        return (x,y)
    
    def order(self):

       return  EC_Order(self.order)
