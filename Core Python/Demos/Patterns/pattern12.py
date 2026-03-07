for i in range(1,6):
    for j in range(1,6):
        if(i==1 or j==1 or i==5 or j==5 or i==j or i+j==6):   #for left diagnonal i==j
            print("*",end= " ")                               # for right diagonal i+j==6
        else:
            print(" ",end = " ")
    print()

'''
* * * * *
* *   * *
*   *   *
* *   * *
* * * * *

'''
