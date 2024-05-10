def singleton_decorator(class_):
    _instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)

        return _instances[class_]

    return wrapper
