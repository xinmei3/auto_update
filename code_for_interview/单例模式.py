class Singleton(object):
    instance = {}

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance


A = Singleton(18, "dongge")
B = Singleton(8, "dongge")

print(id(A), id(B))
