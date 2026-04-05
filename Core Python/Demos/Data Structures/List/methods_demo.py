li = [5,4,1,18,50,18]

#append
li.append(10)
print(li)

#clear
# li.clear()
# print(li)

#copy
li1 = li.copy()
print(li1)

print(f"id of li {id(li)}")
print(f"id of li1 {id(li1)}")

#count   ---- how many types repeated that number or string

print(li.count(18))


# extend  ----- add multiple elemnts at the end of list
li.extend([100,200])
print(li)


# insert ---- add the elemnts uisng index position  #(index,value)

li.insert(1,20)
print(li)

#index ----- find position of elemnt

print(li.index(100))

# pop ----   remove elemnt using index  #pop(index)
li.pop(5)
print(li)

#remove  ------ removes  by value
li.remove(18)
print(li)


# reverse
li.reverse()
print(li)

#sort     reverse = true ---> descendiing order
          #reverse = false ---> acsending order
li.sort(reverse=False)
print(li)
