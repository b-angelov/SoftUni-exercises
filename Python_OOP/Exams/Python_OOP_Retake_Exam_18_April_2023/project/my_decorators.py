


class MyDecoratorsMxn:
    @staticmethod
    def __raise_error(message, exc, condition):
        if condition:
            raise exc(message)

    @staticmethod
    def check_str(error_message):
        """
            Checking whether property string value is empty, raise ValueError if so
            \nExample:
                @my_property.setter\n
                @MyDecoratorsMxn.check_str('My Error message if value is empty')\n\n
                def my_property(self, value):
                    self.__mp = value
        """

        def decorator(func):
            def inner(self, value):
                MyDecoratorsMxn.__raise_error(error_message, ValueError, not value.strip())
                return func(self, value)
            return inner
        return decorator

    @staticmethod
    def __condition(first, second, less_greater_equal_condition = "l"):
        reference_dct = {"l": lambda a, b: a < b,
                         "le": lambda a, b: a <= b,
                         "g": lambda a, b: a > b,
                         "ge": lambda a, b: a >= b}
        return reference_dct[less_greater_equal_condition](first, second)

    @staticmethod
    def check_int(error_message, referent_value, less_greater_equal_condition="l"):
        """Compares numeric property value, according to provided reference value and condition.
            Due to Literal absence in versions prior python 3.8, optional comparison parameters are given as follows:
                Literal["l", "le", "g", "ge"] = "l"

            \nExample:
                @my_property.setter\n
                @MyDecoratorsMxn.check_str('My Error message if value is empty',0,'le')\n\n
                def my_property(self, value):
                    self.__mp = value"""

        def decorator(func):
            def inner(self, value):
                cond = MyDecoratorsMxn.__condition(value, referent_value, less_greater_equal_condition)
                MyDecoratorsMxn.__raise_error(error_message, ValueError, cond)
                return func(self, value)
            return inner
        return decorator

    @staticmethod
    def check_result_int(error_message, referent_value,less_greater_equal_condition="l"):
        """Compares result of a numeric property value set, according to provided reference value and condition.
            Due to Literal absence in versions prior python 3.8, optional comparison parameters are given as follows:
                Literal["l", "le", "g", "ge"] = "l"
        \nExample:
                @my_property.setter\n
                @MyDecoratorsMxn.check_str('My Error message if value is empty',0,'le')\n\n
                def my_property(self, value):
                    self.__mp = value"""

        def decorator(func):
            def inner(self, value):
                try:
                    value += self.__dict__[f"__{func.__name__}"]
                except KeyError:
                    pass
                cond = MyDecoratorsMxn.__condition(value, referent_value, less_greater_equal_condition)
                MyDecoratorsMxn.__raise_error(error_message, ValueError, cond)
                return func(self, value)
            return inner
        return decorator

    @staticmethod
    def get_from_collection(attr_name: str, desired_attr_value, collection, single_element=True):
        if single_element:
            return next((item for item in collection if getattr(item, attr_name) == desired_attr_value), None)
        else:
            return list(item for item in collection if getattr(item, attr_name) == desired_attr_value)

    @staticmethod
    def get_from_collection_or_raise(*args, message, exc=Exception):
        result = MyDecoratorsMxn.get_from_collection(*args)
        if not result:
            MyDecoratorsMxn.__raise_error(message, exc, True)
        return result

    @staticmethod
    def add_to_collection(item: object, collection: [object]):
        collection.append(item)

    @staticmethod
    def remove_from_collection(item: object, collection: [object], message="", exc=Exception):
        try:
            collection.remove(item)
        except:
            MyDecoratorsMxn.__raise_error(message, exc, True)

    @staticmethod
    def remove_from_collection_by_attribute(attr_name: str, desired_attr_value: str, collection, *args, **kwargs):
        obj = []
        obj.extend(
            MyDecoratorsMxn.get_from_collection_or_raise(attr_name, desired_attr_value, collection, *args, **kwargs))
        for ob in obj:
            collection.remove(ob)

if __name__ == "__main__":
    pass
