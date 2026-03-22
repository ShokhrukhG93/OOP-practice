# Defining a class A, and two subclasses B and C of A
class A:
    # Initialize an object of class A with attributes att1 and att2
    def __init__(self, att1, att2):
        self.att1, self.att2 = att1, att2

    # Method act defined in Class A
    def act(self):
        print('The act defined in Class A')

# Defining subclass B of A
class B(A):
    # Initialize an object of class B with attributes att1, att2 and att3
    def __init__(self, att1, att2, att3):
        super().__init__(att1, att2) # Call the constructor of class A
        self.att3 = att3
    
# Defining subclass C of A
class C(A):
    # Initialize an object of class C with attributes att1, att2 and att4
    def __init__(self, att1, att2, att4):
        super().__init__(att1, att2)
        self.att4 = att4

# Defining subclass D of C
class D(C):
    # Initialize an object of class C with attributes att1, att2, att4 and att5
    def __init__(self, att1, att2, att4, att5):
        super().__init__(att1, att2, att4)
        self.att5 = att5
