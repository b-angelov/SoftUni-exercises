def exc(condition, message="", error=Exception, negate_condition=True):
    if negate_condition:
        condition = not condition
    if condition:
        raise error(message)


def string_is_empty(message, error=ValueError):
    def decorator(func):
        def wrapper(self, value, *args, **kwargs):
            exc(value.strip(), message, error)
            return func(self, value, *args, **kwargs)

        return wrapper

    return decorator


def value_in_inclusive_range(min, max, message, error=ValueError):
    def decorator(func):
        def wrapper(self, value, *args, **kwargs):
            exc(min <= value <= max, message, error)
            return func(self, value, *args, **kwargs)

        return wrapper

    return decorator


def is_below_zero(message, error=ValueError):
    def decorator(func):
        def wrapper(self, value, *args, **kwargs):
            exc(value < 0, message, error, negate_condition=False)
            return func(self, value, *args, **kwargs)

        return wrapper

    return decorator

def is_in_collection(attr_name, attr_value, collection, mesasage_if_missing):
    obj = next((obj for obj in collection if getattr(obj, attr_name) == attr_value), None)
    if obj:
        return obj
    return mesasage_if_missing

