def singleton(cls):
    cls.__instance__ = None
    cls.__firstinit__ = True

    def init_decorator(func):
        def wrapper(*args, **kwargs):
            if not cls.__firstinit__:
                return
            func(*args, **kwargs)
            cls.__firstinit__ = False
        return wrapper

    def new_decorator(func):
        def wrapper(cls_, *args, **kwargs):
            if cls.__instance__ is None:
                cls.__instance__ = func(cls_, *args, **kwargs)
            return cls.__instance__
        return wrapper

    cls.__init__ = init_decorator(cls.__init__)
    cls.__new__ = new_decorator(cls.__new__)

    return cls
