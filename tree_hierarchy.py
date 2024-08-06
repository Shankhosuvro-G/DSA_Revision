class Treenode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_hierarchy(self,property_name):
        if property_name == "both":
            value=self.name+" "+self.designation
        elif property_name == "name":
            value=self.name
        else:
            value=self.designation
        spaces=' '*self.get_level()*3
        prefix=spaces+"|__" if self.parent else ""
        print(prefix+value)
        if self.children:
            for child in self.children:
                child.print_hierarchy(property_name)
def build_hierarchy():
    Infra_head=Treenode("Vishwa","Infrastructure Head")
    Infra_head.add_child(Treenode("Dhaval","Cloud Manager"))
    Infra_head.add_child(Treenode("Abhijit","App Manager"))

    cto=Treenode("Chinmay","CTO")
    cto.add_child(Infra_head)
    cto.add_child(Treenode("Aamir","Application Head"))
                  
    hr=Treenode("Gels","HR Head")
    hr.add_child(Treenode("Peter","Recruitment Manager"))
    hr.add_child(Treenode("Waqas","Policy Manager"))
    
    ceo=Treenode("Nilupul","CEO")
    ceo.add_child(cto)
    ceo.add_child(hr)

    return ceo
if __name__=='__main__':
    root_node=build_hierarchy()
    root_node.print_hierarchy("name")
    root_node.print_hierarchy("designation")
    root_node.print_hierarchy("both")


    


        