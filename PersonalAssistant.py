class PersonalAssistant:  
  def __init__(self, todos):
    
    self.todos = todos

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name "

  def add_todo(self, new_item):
    self.todos.append(new_item)
    

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
    # Get the todo_item index in list
      index = self.todos.index(todo_item)
    # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
     print("Todo is not in list!")

  def get_todo(self):
    return self.todos

  def get_birthday(self, name):
    if name == "Len":
      print("Birthday is 02/23/01")
    elif name == "Joi":
      print("Birthday is 08/28/89")
    elif name == "Michelle":
      print("Birthday is 05/19/82")
    else:
      print("Can't find a birthday for this person")


# # Code to test output of the class
# assistant = PersonalAssistant()
# assistant.add_todo("Pick up groceries")
# print(assistant.get_todo())
# # Change name to one from your contacts
# print(assistant.get_contact("Chelsea"))
# print(assistant.get_birthday("Michelle"))

