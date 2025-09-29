class OperationRegistry:
    _registry = {}

    @classmethod
    def add(cls, operation, op_class):
        cls._registry[operation] = op_class

    @classmethod
    def get(cls, operation):
        return cls._registry.get(operation)

    @classmethod
    def get_registry(cls):
        return cls._registry

    @staticmethod
    def register(operation):
        def wrapper(cls):
            OperationRegistry.add(operation, cls)
            return cls

        return wrapper
