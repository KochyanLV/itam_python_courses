def debug_control(*args, **kwargs):
    str_, float_, int_ = 0, 0, 0
    for i in args:
        if type(i) == str: str_+=1
        if type(i) == int: int_+=1
        if type(i) == float: float_+=1
    for i in kwargs:
        if type(i) == str: str_+=1
        if type(i) == int: int_+=1
        if type(i) == float: float_+=1
    print(f'str: {str_}, int: {int_}, float: {float_}')
    
debug_control("Hello!", 1000, 7, 993.0, name="Petr", task="Eliminate")
