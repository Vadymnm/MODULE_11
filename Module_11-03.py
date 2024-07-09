
import pprint
import inspect


def introspection_info(obj):
    print('obj =', obj)

    d = {'Type': type(obj), 'attr': dir(obj), 'module': inspect.ismodule(obj),
         'function': inspect.isfunction(obj)}
    return d


def func_(x):
    y = x**2
    return y


a = func_(37)

obj_info = introspection_info(a)
print()
pprint.pprint(obj_info)

print('-----------------------------------')
print(type(obj_info))
print(inspect.getmodule(introspection_info))
pprint.pprint(inspect.signature(introspection_info))
print('-----------------------------------')
