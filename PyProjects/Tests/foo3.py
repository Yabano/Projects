import os, sys; sys.path.insert(0, os.path.dirname(__file__)) # needed for some interpreters

def function_a():
    print("a1")
    from foo3 import function_b
    print("a2")
    function_b()
    print("a3")

def function_b():
    print("b")

print("t1")
print("m1")
function_a()
print("m2")
print("t2")