class Triangle:
    def __init__(self,a,b,c):
        self.a,self.b,self.c = a,b,c

    def get_area(self):
        a, b, c = self.a,self.b,self.c
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))*0.5