for i in range(1,6):
    for j in range(i,5+1):
            if(j==i or j==5 or i==1):      #i==1  ----- for print first row
                print(j,end=" ")           
            else:
                 print(" ",end=" ")
    print()
