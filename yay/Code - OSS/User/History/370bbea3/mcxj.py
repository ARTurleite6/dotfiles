class LesserOrEqualIdentation(Exception):
    def __init__(self, message):
        super.__init__(message)

class AST():
    def __init__(self, identation: int = 0, children: list["AST"] = []):
        self.identation = identation
        self.children = []
        for child in children:
            self.add_child(child)

    def add_child(self, child: "AST"):
        if child.identation <= self.identation:
            raise LesserOrEqualIdentation("Para adicionar um bloco a identacao do filho deve ser maior que o do pai")
        self.children.append(child)

class Block(AST):
    def __init__(self, tag: str = "div", attributes: list[str] = [], content: str = "", identation: int = 0, children: list["Block"] = [], identifiers: list[str] = []):
        super().__init__(identation, children)
        self.tag = tag
        self.attributes = attributes 
        self.content = content
        self.classes = list(map(lambda x: x[1:], filter(lambda x: x[0] == '.', identifiers)))
        self.ids = list(map(lambda x: x[1:], filter(lambda x: x[0] == '#', identifiers)))

    def __str__(self) -> str:
        result = " " + " ".join(self.attributes) if len(self.attributes) != 0 else ""
        classes = " ".join(self.classes)
        class_str = f" class=\"{classes}\"" if classes else ""
        ids = " ".join(self.ids)
        ids_str = f" id=\"{ids}\"" if ids else ""
        content = self.content if len(self.children) == 0 else "\n".join(map(lambda x: str(x), self.children))
        identation_str = " " * self.identation
        return f"{identation_str}<{self.tag}{class_str}{ids_str}{result}>\n{content}\n{identation_str}</{self.tag}>"
