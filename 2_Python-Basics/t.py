

class W:
      R=dict()
      def __init__(self, id) -> object:
            che= self.check(id)
            if che is not False:
                  return self.check(id)
            else:
                  self.id = id
                  self.stock = []
                  W.R[id]={self : self.stock}
                  
            
      @staticmethod
      def check(id):
            for k, v in W.R.items() :
                  if id==k:
                        return v.keys()
            return False  
      
w=W(1)
q=W(2)
print(w, q, W.R, sep='\n')
e=W(1)
print(e, W.R)