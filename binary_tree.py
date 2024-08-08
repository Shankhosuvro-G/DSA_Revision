class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        #Checking for the value if it already exists
        if self.data==data:
            return "Data already exists"
        if data < self.data:
            #Go to the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        if data > self.data:
            #Go to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    def search(self,data):
        if self.data==data:
            return True
        if data < self.data:
            #go to the left subtree
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            #go to the right subtree
            if self.right:
                return self.right.search(data)
            else:
                return False
        return False
    def in_order_traversal(self):
        elements=[]
        #First go to left subtree
        if self.left:
            elements.extend(self.left.in_order_traversal())
        #Secondly go the base element
        elements.append(self.data)
        #Finally go to the left subtree
        if self.right:
            elements.extend(self.right.in_order_traversal())
        return elements
    def post_order_traversal(self):
        elements=[]
        #First go to the left subtree
        if self.left:
            elements.extend(self.left.post_order_traversal())
        #Secondly go to the right subtree
        if self.right:
            elements.extend(self.right.post_order_traversal())
        elements.append(self.data)
        return elements
    def pre_order_traversal(self):
        #First add the base element
        elements=[self.data]
        #Secondly go to the left subtree
        if self.left:
            elements.extend(self.left.pre_order_traversal())
        #Finally go to the right subtree
        if self.right:
            elements.extend(self.right.pre_order_traversal())
        return elements
    def find_min(self):
        #For finding the minimum go to the left subtree
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()
    def find_max(self):
        #For finding the maximum go to the right subtree
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
    def calculate_sum(self):
        left_sum=0
        right_sum=0
        #Calcularing the sum for the left subtree
        if self.left:
            left_sum=self.left.calculate_sum() if self.left else 0
        #Calculating the sum for right subtree
        if self.right:
            right_sum=self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum   
    def check_bst(self):
        def solve(node,left,right):
            if not node:
                return True
            if node.data > left and node.data < right:
                return solve(node.left,left,node.data) and solve(node.right,node.data,right)
        return solve(self,float("-inf"),float("inf"))
    def check_sum_tree(self):
        left_sum=0
        right_sum=0
        if self.left:
            left_sum=self.left.calculate_sum() if self.left else 0
        if self.right:
            right_sum=self.right.calculate_sum() if self.right else 0
        if self.data==left_sum+right_sum:
            is_left_sum=self.left.check_sum_tree() if self.left else True
            is_right_sum=self.right.check_sum_tree() if self.right else True
            return is_left_sum and is_right_sum
        return False
    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left=self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right=self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            #Find the minimum value
            min_val=self.left.find_min()
            #Copy the minimum value
            self.data=min_val
            #Update self.right
            self.right=self.delete(min_val)
        return self        
        
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
    
if __name__=="__main__":
    elements = [17, 4, 20, 1, 9, 18, 23, 34, 19, 22, 6]
    tree = build_tree(elements)
    
    # Test Case 1: In-Order Traversal
    assert tree.in_order_traversal() == [1, 4, 6, 9, 17, 18, 19, 20, 22, 23, 34], "Test Case 1 Failed"
    print("Test Case 1 Passed")

    # Test Case 2: Pre-Order Traversal
    assert tree.pre_order_traversal() == [17, 4, 1, 9, 6, 20, 18, 19, 23, 22, 34], "Test Case 2 Failed"
    print("Test Case 2 Passed")

    # Test Case 3: Post-Order Traversal
    assert tree.post_order_traversal() == [1, 6, 9, 4, 19, 18, 22, 34, 23, 20, 17], "Test Case 3 Failed"
    print("Test Case 3 Passed")

    # Test Case 4: Search for existing element
    assert tree.search(19) == True, "Test Case 4 Failed"
    print("Test Case 4 Passed")

    # Test Case 5: Search for non-existing element
    assert tree.search(25) == False, "Test Case 5 Failed"
    print("Test Case 5 Passed")

    # Test Case 6: Find minimum value
    assert tree.find_min() == 1, "Test Case 6 Failed"
    print("Test Case 6 Passed")

    # Test Case 7: Find maximum value
    assert tree.find_max() == 34, "Test Case 7 Failed"
    print("Test Case 7 Passed")

    # Test Case 8: Calculate sum of all nodes
    assert tree.calculate_sum() == 173, "Test Case 8 Failed"
    print("Test Case 8 Passed")

    # Test Case 9: Check if it's a valid BST
    assert tree.check_bst() == True, "Test Case 9 Failed"
    print("Test Case 9 Passed")

    # Test Case 10: Check if it's a sum tree (Expect False)
    assert tree.check_sum_tree() == False, "Test Case 10 Failed"
    print("Test Case 10 Passed")

    # Test Case 11: Delete a node
    tree.delete(9)
    assert tree.in_order_traversal() == [1, 4, 6, 17, 18, 19, 20, 22, 23, 34], "Test Case 11 Failed"
    print("Test Case 11 Passed")


