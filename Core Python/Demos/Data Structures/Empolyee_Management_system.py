def addEmp(id, name, sal, dept):
    if(id not in emp_detail):
        emp_detail[id] = [id, name, sal, dept]
        return 'Employee added successfully.'
    else:
        return f'{id} already available.'

def updEmp(id):
    if(id in emp_detail):
        emp = emp_detail[id]
        print("Note: If don't want to change the field, leave blank.")
        name = input(f'Enter new name({emp[1]}):') or emp[1]
        sal = float(input(f'Enter new sal({emp[2]}):')) or emp[2]
        dept = input(f'Enter new dept({emp[3]}):') or emp[3]
        emp_detail[id] = [id, name, sal, dept]
        return 'Employee updated successfully.'
    else:
        return f'{id} not exists.'

def delEmp(id):
    if(id in emp_detail):
        del emp_detail[id]
        print(f"{id} deleted successfully")

    else:
        print(f"{id} not found")


def searchEmp(id):
    if (id in emp_detail):
        emp = emp_detail[id]
        print("Employee Found:")
        print(f"ID: {emp[0]}")
        print(f"Name: {emp[1]}")
        print(f"Salary: {emp[2]}")
        print(f"Department: {emp[3]}")
    else:
        print(f'{id} not found.')



emp_detail = {}
ch = 0
while(ch != '6'):
    print('''Please select option:
    1. Add emp
    2. Show all emp
    3. Update emp
    4. Delete emp
    5. Search emp
    6. Exit
    ''')
    ch = input('Enter choice:')
    if(ch == '1'):
        id = input('Enter ID:')
        name = input('Enter NAME:')
        sal = float(input('Enter SALARY:'))
        dept = input('Enter DEPARTMENT:')
        res = addEmp(id, name, sal, dept)
        print(res)
    elif(ch == '2'):
        print(emp_detail)
    elif(ch == '3'):
        id = input('Enter ID:')
        res = updEmp(id)
        print(res)
    elif(ch == '4'):
        id = input("Enter ID: ")
        res = delEmp(id)
        print(res)
    elif(ch == '5'):
        id = input("Enter ID: ")
        searchEmp(id)
    elif(ch == '6'):
        print('Mandal abhari ahe!!!!!!!!')
    else:
        print('Invalid choice.....')
