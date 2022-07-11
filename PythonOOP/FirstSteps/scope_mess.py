x = "global"


def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        x = "global: changed!"
        print(x)

    print("outer:", x)
    inner()
    print("outer:","nonlocal")
    change_global()


print(x)
outer()

'''
global 
outer: local 
inner: nonlocal 
outer: nonlocal 
global: changed!
'''
