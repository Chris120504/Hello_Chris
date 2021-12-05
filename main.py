# This is a test code
class Chris:
  # Define a human called Chirs
   def __init__(self, name, age, email, money):
    self.name = name
    self.age = age
    self.email = email
    self.money = money
    
    def about(self):
      print("My name: " + self.name)
      print("My age: " + self.age)
      print("My email: " + self.email)
      print("My money: " + self.money)
      
if __name__ == "__main__":
  # Time 12/4/2021
  me = Chris("Chris", "9", "Chris@boba.cat", "120")
  
