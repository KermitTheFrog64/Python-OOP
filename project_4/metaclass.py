class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name,
                future_class_parents, future_class_attr):

        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        # используем метод type.__new__
        # базовое ООП, никакой магии
        return type.__new__(upperattr_metaclass, future_class_name,
                            future_class_parents, uppercase_attr)




class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return type.__new__(cls, name, bases, uppercase_attr)