import os

def check_lists(function):
    def check(**kwargs):
        condition = kwargs.get("error_raise_condition",True)
        no_error = kwargs.get("do_not_raise_error", False)
        name = kwargs.get("name",True)
        attr1 = kwargs.get("attr1",name)
        name1 = kwargs.get("name1",name)
        att = kwargs.get("attr",name)
        excp = kwargs.get("exc",Exception)
        ob = [value for value in kwargs["collection"] if function(getattr(value, att, name),name) and function(getattr(value,attr1,name1),name1)]
        if condition:
            condition = bool(ob)
        else:
            condition = bool(not ob)
        if not no_error:
            exc(kwargs.get("error_message", ""),condition,excp)
        return ob[kwargs.get("item",0)] if ob else False
    return check

@check_lists
def check_collections(cond, val, op ="=="):
    if op == "==":
        return cond == val
    if op == "!=":
        return cond != val

def raise_exception(function):
    def e_raise(message, condition, error=ValueError):
        if function(condition):
            raise error(message)

    return e_raise


@raise_exception
def exc(cond):
    if cond: return True

def zip_current_project():
    path = os.path.dirname(os.path.realpath(__file__))
    os.system("tar --exclude __pycache__ -acvf project.zip project")

def get_from_collection_or_error(*args,**kwargs):
    kwargs.update(dict(zip(["collection","att","name","message","exc","error_raise_condition"],args)))
    arguments = kwargs
    return check_collections(**arguments)

def is_in_collection(*args,**kwargs):
    return bool(get_from_collection_or_error(*args, **kwargs, do_not_raise_error=True))

def is_not_in_collection(*args,**kwargs):
    return False if is_in_collection(*args, **kwargs) else True

def not_in_collection_or_error(*args,**kwargs):
    return get_from_collection_or_error(*args,**kwargs,error_raise_condition=False)

sep = lambda message,new_lines=1,symbols=10,sym="#": print(("\n" * new_lines) + (sym * symbols) + message.upper() + (sym * symbols), end = "\n" * new_lines)
