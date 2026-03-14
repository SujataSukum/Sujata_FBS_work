def dummy(*args,**kwargs):
    print(args)
    print(kwargs)

dummy(10,20,30,40,id=101,name='ABC',sal=70000)
