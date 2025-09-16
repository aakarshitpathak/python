class vectors:
    def __init__(self,l):
        self.l=l
    
    def __len__(self):
        return len(self.l)
    
# Test the implementation 
v1 = vectors([1,2,3])
print(len(v1))