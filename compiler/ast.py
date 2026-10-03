class Program:
    def __init__(self, declarations=None):
        self.declarations = declarations or []

    def __repr__(self):
        return f"Program({self.declarations!r})"


class ClassDeclaration:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

    def __repr__(self):
        return f"ClassDeclaration({self.name!r}, {self.members!r})"


class MethodDeclaration:
    def __init__(self, return_type, name, parameters=None, body=None):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters or []
        self.body = body or []

    def __repr__(self):
        return (
            f"MethodDeclaration("
            f"{self.return_type!r}, "
            f"{self.name!r}, "
            f"{self.parameters!r}, "
            f"{self.body!r})"
        )


class ObjectDeclaration:
    def __init__(self, class_name, object_name):
        self.class_name = class_name
        self.object_name = object_name

    def __repr__(self):
        return (
            f"ObjectDeclaration("
            f"{self.class_name!r}, "
            f"{self.object_name!r})"
        )