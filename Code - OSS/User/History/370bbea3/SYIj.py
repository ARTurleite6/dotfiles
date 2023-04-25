class LesserOrEqualIdentation(Exception):
    def __init__(self, message):
        super.__init__(message)

class AST():
    def __init__(self, identation: int = 0, children: list["AST"] = []):
        self.identation = identation
        self.children = children

class Block(AST):
    def __init__(self, tag: str = "div", attributes: list[str] = [], content: str = "", identation: int = 0, children: list["Block"] = [], identifiers: list[str] = []):
        super().__init__(identation, children)
        self.tag = tag
        self.attributes = attributes 
        self.content = content
        self.classes = list(map(lambda x: x[1:], filter(lambda x: x[0] == '.', identifiers)))
        self.ids = list(map(lambda x: x[1:], filter(lambda x: x[0] == '#', identifiers)))
        

    def add_child(self, block: "Block"):
        if block.identation <= self.identation:
            raise LesserOrEqualIdentation("Para adicionar um bloco a identacao do filho deve ser maior que o do pai")
        self.children.append(block)

    def __str__(self) -> str:
        result = " " + " ".join(self.attributes) if len(self.attributes) != 0 else ""
        classes = " ".join(self.classes)
        class_str = f" class=\"{classes}\"" if classes else ""
        ids = " ".join(self.ids)
        ids_str = f" id=\"{ids}\"" if ids else ""
        return f"<{self.tag}{class_str}{ids_str}{result}>{self.content}</{self.tag}>"
