# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected

    # public function to show the details
    def show(self):
        print("The code of the company is = ")

    # destructor
    def __del__(self):
        print("destructor invoked 1")

# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal,)
        self.__func()       # invoking private method

    def __func(self):
        print("Private class")

    # destructor
    def __del__(self):
        print("destructor invoked 2")

# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name," is working on ",e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()



# misc
bigList = [[1, 3, 6], [8, 2,], [0, 4, 7, 10], [1, 5, 2], [6]]

for i in bigList:
	for j in i:
		print ("Element of list within a list - ", j)

for i in range(10):
    print(i)

triangle = ''
for i in range(1, 6):
    triangle = triangle + (str(i))
    print(triangle)

for i in range(5,0,-1):
    triangle = ''
    while i>0:
        triangle = triangle + (str(i))
        i-=1
    print(triangle)
