
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def print_tree(self):
        spaces = ' ' * self.getlevel() *3
        prefix = spaces + "|->" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
                 

def build_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Macintosh"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone=TreeNode(("Cell Phone"))
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Samsung"))
    cellphone.add_child(TreeNode("Nokia"))

    tv=TreeNode(("Television"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Hikvision"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


if __name__ == "__main__":
    root=build_tree()
    root.print_tree()
    pass




