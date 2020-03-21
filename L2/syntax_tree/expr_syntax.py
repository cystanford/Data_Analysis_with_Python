# 每个函数，都有env参数
Num = lambda env, n: n 
Var = lambda env, x: env[x] 
Add = lambda env, a, b:_eval(env, a) + _eval(env, b) 
Mul = lambda env, a, b:_eval(env, a) * _eval(env, b) 
# 对表达式进行处理，expr[0]为符号，*expr[1:]为传入的参数
_eval = lambda env, expr:expr[0](env, *expr[1:]) 
  
env = {'a':3, 'b':6} 
tree = (Add, (Var, 'a'), 
        (Mul, (Num, 5), (Var, 'b'))
       ) 

print(_eval(env, (Var, 'a')))
print(_eval(env, (Num, 5)))
print(Num(env, 5))
print(_eval(env, tree))
