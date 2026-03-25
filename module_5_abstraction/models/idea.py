# Import the abstract base class module
import abc
from abc import ABC

# Define an abstract base class 'Idea' using inheritance from 'ABC' class
class Idea(ABC):
  # Abstract method 'done', which must be implemented by any subclass
  @abc.abstractmethod
  def done(self):
    pass

# Class 'G1' inherits from 'Idea', but does not implement the 'done' method
class G1(Idea):
  def work(self):
    print("I'm working on it!")

# Class 'G2' inherits from 'G1', overriding the 'work' method
class G2(G1):
  def work(self):
    print("I'm still working on it!")

# Class 'G3' inherits from 'G2' and implements the abstract 'done' method
class G3(G2):
  # 'done' method implementation
  def done(self):
    print("I got it done!")

# Instances of G1 and G2 cannot be created because they are abstract
# Attempting to create an instance of G1 or G2 would raise an error

# Cannot create g1
# g1 = G1()  # Uncommenting this would raise an error

# Cannot create g2
# g2 = G2()  # Uncommenting this would raise an error

# Instance of G3 can be created since it implements the 'done' method
g3 = G3()
g3.work()  # Calls the 'work' method from G2
g3.done()  # Calls the 'done' method from G3