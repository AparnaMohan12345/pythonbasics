class myclass:
    class_variable = "Hello world"
    @classmethod
    def class_method(cls):
        print(cls.class_variable)
myclass.class_method()