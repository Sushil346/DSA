class TreeNode:
    def __init__(self,name,post):
        self.name = name
        self.post = post
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

    def print_tree_name(self):
        print( self.prefix() + self.name)
        if self.children:
            for child in self.children:
                child.print_tree_name()

    def print_tree_post(self):
        print(self.prefix() + self.post)
        if self.children:
            for child in self.children:
                child.print_tree_post()
    
    def print_tree_all(self):
        print(f"{self.prefix()}{self.name}  ({self.post})")
        if self.children:
            for child in self.children:
                child.print_tree_all()
                 


def build_tree():
    root_nilupul=TreeNode("Nilupal","CEO")
    
    chinmay=TreeNode("Chinmay","CTO")
    gels=TreeNode("Gels","HR Head")

    vishwa=TreeNode("Vishwa","Infrastructure Head")
    aamir=TreeNode("Aamir","Application Head")

    dhaval=TreeNode("Dhaval", "Cloud Manager")
    abhijit=TreeNode("Abhijit","App Manager")

    peter=TreeNode("Peter","Recruitment Manager")
    waqas=TreeNode("Waqas","Policy Manager")

    ### Adding Children
    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)

    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    gels.add_child(peter)
    gels.add_child(waqas)

    ##addomg root children
    root_nilupul.add_child(chinmay)
    root_nilupul.add_child(gels)          

    return root_nilupul


if __name__ == "__main__":
    root=build_tree()

    print("Type: 1 for only name, 2 for only post, 3 for both;\nOther would be invalid:")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\nNames:")
            root.print_tree_name()
        elif choice == 2:
            print("\nPosts:")
            root.print_tree_post()
        elif choice == 3:
            print("\nBoth:")
            root.print_tree_all()
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("\nInvalid input. Enter a number (1, 2, or 3).")





