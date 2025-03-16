class TreeNode:
    def __init__(self,name):
        self.name = name
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
    
    def prefix(self):
        spaces = ' ' * self.getlevel() *3
        Prefix = spaces + "|-->" if self.parent else ""
        return Prefix

    def print_tree_name(self, level):
        if self.getlevel() <= level:
            print( self.prefix() + self.name)
            for child in self.children:
                child.print_tree_name(level)                 


def build_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))
    india.add_child(gujarat)
    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))
    india.add_child(karnataka)

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    usa.add_child(new_jersey)
    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)
    return root


if __name__ == "__main__":
    root=build_tree()

    print("Type level upto which you want to print:")
    try:
        choice = int(input("Level: "))
        # if choice == 0 or choice == 1 or choice == 2 or choice == 3:
        if 0<=choice<=3:  
            root.print_tree_name(choice)

        else:
            print("\nInvalid choice. Please enter valid level")

    except ValueError:
        print("\nInvalid input. Enter a number (0, 1, 2, or 3).")





