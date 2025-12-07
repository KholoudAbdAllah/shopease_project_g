class Singleton:
    _instance = None

    @staticmethod
    def instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance
