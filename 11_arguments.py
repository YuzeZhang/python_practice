def test(a,b,c=100,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
test(11,22,33,44,55,66,77,task=99,done=89)
