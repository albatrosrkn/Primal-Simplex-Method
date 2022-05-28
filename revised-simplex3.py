import numpy as np
def funct():
    iteration=0
    totalvariable= 2
    totalconstant= 2
    objZ= [2,1]
    matrix= [['3', '4', '<=', '6'], ['6', '1','<=', '3']]
    countgreat= 0
    type=1
    
    totalvariable = int(totalvariable)
    totalconstant = int(totalconstant)
    objZ = [int(i) for i in objZ]
    countgreat = int(countgreat)
    eqlCount = 0

    for i in matrix:
        if '=' in i:
            eqlCount += 1
    
    try:
        M=0
        totalvartemp = totalvariable
        objZtemp = objZ
        constNum = totalconstant
        gtemp = countgreat
        objdiff=constNum-eqlCount
    
        for i in range(objdiff):
            objZtemp.append(0)
    
        for i in range(1 + eqlCount):
            objZtemp.append(M)
        c = np.array(objZtemp)*(-1)

        constraints = [] #S1-S2
        slackptr = totalvartemp
    
        artptr = totalvartemp + constNum - eqlCount
    
        SolveValue = []
    
        for i in matrix:
            temp = i
            type = temp[-2]
            SolveValue.append(int(temp[-1]))
            temp.pop()
            temp.pop()
            
            for i in range((gtemp+constNum)):
                temp.append('0')
    
            for i in range(len(temp)):
                temp[i] = int(temp[i])
    
            if '<=' == type:
                temp[slackptr] = 1
                slackptr += 1
            elif '>=' == type:
                temp[slackptr] = -1
                temp[artptr] = 1
                slackptr += 1
                artptr += 1
            elif '=' == type:
                temp[artptr] = 1
                artptr += 1
    
            constraints.append(temp)
     
        Constrainmatrix = np.array(constraints)
       
        SolveMatrix = np.array(SolveValue)

        indexnumber=0
        max=99
        
        for i in c:
            if i<max:
                max=i

        for j in range(0,len(c)):
            if c[j]==max:
                indexnumber=j
        value=[]
        piv2=0
        valuemax=99
        for i in range(0,totalconstant):
            if(Constrainmatrix[i][indexnumber] != 0):
                value.append(SolveMatrix[i]/Constrainmatrix[i][indexnumber])
                if value[i]<valuemax and value[i]>0:
                    valuemax=value[i]
                    piv2=i
        #print(piv2)
        pivelement=Constrainmatrix[piv2][indexnumber] #Pivot Eleman
        #print(pivelement)
        iterpivmatrix=[]
        
        
        for i in range(0,totalvariable+totalconstant):
            iterpivmatrix.append(Constrainmatrix[piv2][i]/pivelement)
        iterZetMatrix=[]
        #S1iter1
        for i in range(0,totalvariable+totalconstant):
            iterZetMatrix.append(c[i]+((-1)*c[indexnumber]*iterpivmatrix[i]))
        
        #S2 iter2
        czmTemp = []
        aTemp=[]
        iternotpivmatrix=[]
        for i in range(0,totalvariable+totalconstant):
            for j in  range(0,totalconstant):
                if j==piv2:
                    continue
                iternotpivmatrix.append(Constrainmatrix[j][i]+((-1)*Constrainmatrix[piv2-1][indexnumber]*iterpivmatrix[i]))
        a=1
        for j in iternotpivmatrix:
            if(a % (totalvariable+totalconstant) == 0 and a!=0):
                try:
                    aTemp.append(j)
                    czmTemp.append(aTemp)
                    aTemp = []
                except:
                    continue
            else:
                aTemp.append(j)
            a=a+1
        Solvepiv=[]
   
        Solvepiv.append(SolveMatrix[piv2]/pivelement)
        #Zet çözüm
        Zetsolve=c[totalconstant+totalvariable]+(((-1)*c[indexnumber])*Solvepiv[0])
        #Çözümmatrix
        #print(SolveMatrix)
        
                    
    
        othersolve=[]
        for i in range(0,totalconstant):
            if i==piv2:
                continue
            othersolve.append(SolveMatrix[i]+((Constrainmatrix[i][indexnumber]*(-1))*Solvepiv[0]))
    
        iterZetMatrix.append(Zetsolve)
        czmTemp.append(iterpivmatrix)

        cozummatrix=[]

        flag=0
        for j in range(0,totalconstant):
            if(j==piv2):
                flag=1
                cozummatrix.append(Solvepiv[0])
            else:
                cozummatrix.append(othersolve[j-flag])      
       
        for i in range(0,totalconstant+totalvariable):
            if iterZetMatrix[i]<0.0:
                iteration=iteration+1
                funct2(iterZetMatrix, czmTemp, cozummatrix, totalvariable, totalconstant, iteration)
        
        if iteration==0:
            print("Problem is solved in",iteration+1,"iteration")
            print("Optimal Value is",iterZetMatrix[totalconstant+totalvariable])
            print("X cozum",cozummatrix)
                
       
    
    except:
        print("Invalid Input or the problem has an infeasible solution.‎")

def funct2(c,Constrainmatrix,SolveMatrix,totalvariable,totalconstant,iteration):
    indexnumber=0
    max=99
    #print("Cons",Constrainmatrix)
    for i in c:
        if i<max:
            max=i
    
    for j in range(0,len(c)):
        if c[j]==max:
            indexnumber=j
    value=[]
    piv2=0
    valuemax=99
    #print(Constrainmatrix)
    for i in range(0,totalconstant):
        if(Constrainmatrix[i][indexnumber] != 0):
            value.append(SolveMatrix[i]/Constrainmatrix[i][indexnumber])
    tk = 0
    for j in value:
        if j<valuemax and j>0:
            valuemax=j
            piv2=tk
        tk=tk+1
    pivelement=Constrainmatrix[piv2][indexnumber] #Pivot Eleman

    iterpivmatrix=[]
    for i in range(0,totalvariable+totalconstant):
        iterpivmatrix.append(Constrainmatrix[piv2][i]/pivelement)
    #print ("iterpivmatrix",iterpivmatrix)
    iterZetMatrix=[]
    
    #S1iter1
    for i in range(0,totalvariable+totalconstant):
        iterZetMatrix.append(c[i]+((-1)*c[indexnumber]*iterpivmatrix[i]))

    
    #S2 iter2
    czmTemp = []
    aTemp=[]
    iternotpivmatrix=[]
    for i in range(0,totalvariable+totalconstant):
        for j in  range(0,totalconstant):
            if j==piv2:
                continue
            iternotpivmatrix.append(Constrainmatrix[j][i]+((-1)*Constrainmatrix[piv2-1][indexnumber]*iterpivmatrix[i]))
        a=1
    for j in iternotpivmatrix:
        if(a % (totalvariable+totalconstant) == 0 and a!=0):
            try:
                aTemp.append(j)
                czmTemp.append(aTemp)
                aTemp = []
            except:
                continue
        else:
            aTemp.append(j)
        a=a+1

    Solvepiv=[]
    #Pivotun çözüm sonucu
    Solvepiv.append(SolveMatrix[piv2]/pivelement)
    #Zet çözüm
    Zetsolve=c[totalconstant+totalvariable]+(((-1)*c[indexnumber])*Solvepiv[0])
    #print("Zetsolve",Zetsolve)
    #Çözümmatrix
    othersolve=[]
    for i in range(0,totalconstant):
            if i==piv2:
                continue
            othersolve.append(SolveMatrix[i]+((Constrainmatrix[i][indexnumber]*(-1))*Solvepiv[0]))
    
    iterZetMatrix.append(Zetsolve)
    #print (othersolve)
    #print(iterZetMatrix)
    cozummatrix=[]
    czmTemp.append(iterpivmatrix)
    flag=0
    for j in range(0,totalconstant):
        if(j==piv2):
            flag=1
            cozummatrix.append(Solvepiv[0])
        else:
            cozummatrix.append(othersolve[j-flag])
    for i in range(0,totalconstant):
        print("X",i+1,":",cozummatrix[i])
    print("Problem is solved in",iteration+1,"iteration")
    print("Optimal Value is",iterZetMatrix[totalconstant+totalvariable])
    for i in range(0,totalconstant+totalvariable):
        if iterZetMatrix[i]<0:
            iteration=iteration+1
            funct2(iterZetMatrix, czmTemp, cozummatrix, totalvariable, totalconstant, iteration)

        
funct()
