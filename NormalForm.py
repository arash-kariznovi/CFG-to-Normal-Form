class NormalForm:

    def __init__(self,productions,product_numbers):
        self.start_variable = "S"
        self.productions = productions
        self.product_numbers = product_numbers
        variables = []
        self.variables = variables
        right = []
        self.right = right
    #every product in a array
    # [0] is variables in left and
    # [1] is terminal or variables in right
        for i in productions:
            l,r = map(str, str(i).split('->'))
            self.right.append(r)
            self.variables.append(l)
        for i in range(self.product_numbers):
           self.productions[i] = [self.variables[i],self.right[i]]
        #print(self.productions)


    #Remove lambda productions
    def remove_lambda(self):
        Vn=[]

        #find variable that produces lambda directly
        for i in range(len(self.productions)):
            if self.productions[i][1] == 'e':
                Vn.append(self.productions[i][0])
        #print(Vn)

        #find variable that produces lambda indirectly
        size = 0
        while len(self.productions) >= size:

            for k in range(len(self.productions)):
                flag = 1
                for i in range(len(self.productions[k][1])):
                    for j in Vn:
                        if str(self.productions[k][1])[i] == j:
                            flag=0
                            break
                        else:
                            flag=1
                    if flag==1:
                        break
                if(flag == 1):
                    #print("not indirect lambda")
                    pass
                else:
                    #print("Indirect lambda")
                    Vn.append(self.productions[k][0])
            size = size +1
        Vn =list(dict.fromkeys(Vn))
        print("Null Variables:",Vn)

        # remove productions with lambda:
        newProduction = []
        for i in range(len(self.productions)):
            if self.productions[i][1] != 'e':
                newProduction.append(self.productions[i])

        print("New Products:",newProduction)
        for i in newProduction:
            for j in i[1]:
                if j in Vn:
                    print( "%s is in LAMBDA group"%(j))




    def remove_unit(self):
        newProduction = []
        midP1=[]
        midP2=[]
        n = int(len(self.productions))
        for i in self.productions:
            for j in self.productions:
                if i[1] == j[0]:
                   newProduction.append(self.productions.index(j))
            for k in newProduction:
                self.productions.append([i[0],self.productions[k][1]])
                #midP1.append([i[0],self.productions[k][1]])
                #self.productions[k][0] = i[0]

            newProduction=[]
        for i in self.productions:
            if i[1].isupper() and len(i[1])==1:
                self.productions.remove(i)

        print(self.productions)
        print(midP1)

    def remove_useless(self):

#variables reach Terminals directly
        Vt = []
        for i in range(len(self.productions)):
            if not self.productions[i][1].isupper():
                Vt.append(self.productions[i][0])


        #variables reach Terminals indirectly
        size = 0
        while len(self.productions) >= size:

            for k in range(len(self.productions)):
                flag = 1
                for i in range(len(self.productions[k][1])):
                    for j in Vt:
                        if str(self.productions[k][1])[i] == j:
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        break
                if (flag == 1):
                    # print("not indirect lambda")
                    pass
                else:
                    # print("Indirect lambda")
                    Vt.append(self.productions[k][0])
            size = size + 1
        Vt = list(dict.fromkeys(Vt))

        for i in self.productions:
            if i[0] not in Vt:
                self.productions.remove(i)
        print(self.productions)


#eliminate which can't be reached
        Vs = ["S"]
        flag = 1
        while flag == 1:
            flag = 0
            for i in range(len(self.productions)):
                if (self.productions[i][0] in Vs) and self.productions[i][1] not in Vs:
                    if self.productions[i][1].isupper():
                        Vs.append(self.productions[i][1])
                        flag = 1
                else:
                    flag = 0
        for i in self.productions:
            if i[0] not in Vs:
                self.productions.remove(i)
        print(self.productions)


