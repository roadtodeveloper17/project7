class User:
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email

  def __str__(self):
    return f"ID: {self.id} | NAME: {self.name} | EMAIL: {self.email}"

class UserManager:
  def __init__(self):
    self.users = []
    self.new_id = 1

  def add_user(self):
    name = input("Enter name: ")
    if not name:
      print("Invalid name")
      return

    email = input("Enter mail: ")
    if not email:
      print("Invalid mail")
      return

    user = User(self.new_id, name, email)
    self.users.append(user)
    self.new_id += 1
    print("User successfully added")

  def view_users(self):
    if not self.users:
      print("No users found")
      return
    
    print("List of users:")
    for user in self.users:
      print(user)

  def delete_user(self):
    self.view_users()

    try:
      choice = int(input("Choose by an id: "))
      if not choice:
        print("Invalid id")
        return

      user = next((user for user in self.users if user.id == choice), None)

      if user == None:
        print("Invalid id")
        return

      self.users.remove(user)
      print("User successfully deleted")
    except ValueError:
      print("Invalid choice")
      return

def main():
  manager = UserManager()

  while True:
    print("1. Add user")
    print("2. View users")
    print("3. Delete user")
    print("4. Exit")

    try:
      choice = int(input("Choose action: "))

      if choice < 1 or choice > 4:
        print("Invalid choice")
        return

      if choice == 1:
        manager.add_user()
        print()
      elif choice == 2:
        manager.view_users()
        print()
      elif choice == 3:
        manager.delete_user()
        print()
      elif choice == 4:
        print("Exiting...")
        break
    except ValueError:
      print("Invalid action")
      return
      
if __name__ == "__main__":
  main()






































