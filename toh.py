class TOH():

    def __init__(self,n=3):
        self.number_of_pegs = 3
        self.number_of_rings = n
        self.pegs = {}
        self.pegs['A'] = []
        self.pegs['B'] = []
        self.pegs['C'] = []
        self.steps = []
        for i in range(1,n+1):
            self.pegs['A'].append(n+1-i)
        # print("Initial condition ",self.pegs)
        self.steps.append({'A':self.pegs['A'][:],'B':self.pegs['B'][:],'C':self.pegs['C'][:]})

    def getAuxPeg(self,peg1,peg2):
        t = ['A','B','C']
        t.remove(peg1)
        t.remove(peg2)
        return t[0]
    
    def move(self,peg1, peg2, n):
        
        if n == 1:
            temp = self.pegs[peg1].pop()
            self.pegs[peg2].append(temp)
            # print(self.pegs)
            self.steps.append({'A':self.pegs['A'][:],'B':self.pegs['B'][:],'C':self.pegs['C'][:]})
        
        else:
            aux_peg = self.getAuxPeg(peg1,peg2)
            self.move(peg1,aux_peg,n-1)
            self.move(peg1,peg2,1)
            self.move(aux_peg,peg2,n-1)
    
    def solve(self):
        self.move('A','B',self.number_of_rings)

n = int(input("input = "))
t1 = TOH(n)
t1.solve()

steps = t1.steps

for i in range(0,len(steps)):
    if i == 0: 
        print("Initial condition =",steps[i]["A"],steps[i]["B"],steps[i]["C"])
    else:
        print(f"Step {i} =",steps[i]["A"],steps[i]["B"],steps[i]["C"])
         