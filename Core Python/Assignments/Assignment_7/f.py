for i in range(1,6):
    for j in range(i,5+1):
            if(j==i or j==5 or i==1):      #i==1  ----- for print first row
                print(j,end=" ")
            else:
                 print(" ",end=" ")
    print()

'''
1 2 3 4 5
2     5
3   5
4 5
5
'''
