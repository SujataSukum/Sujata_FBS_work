for i in range(1,6):
    for j in range(1,i):        # or we  ca use for j in range(2,i+1)
        print(" ",end=" ")      #bthis loop for increment pattern

    for j in range(1,7-i):
        print("*",end=" ")      # this loop for decremnt pattern

    print()

'''
* * * * *
  * * * *
    * * *
      * *
        *
        
'''
