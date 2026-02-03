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

  def add_user(self, name, email):
    if not name:
        print("No name")
        return
    if not email:
        print("No mail")
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

  def find_user_by_id(self, user_id):

    for user in self.users:
      if user.id == user_id:
        return user
    
    return None
  
  def delete_user(self, user_id):
    user = self.find_user_by_id(user_id)
    
    if not user:
        print("User not found")
        return
    
    self.users.remove(user)
    print("User successfully deleted")
  

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
        continue

      if choice == 1:
        name = input("Enter name: ")
        email = input("Enter mail: ")
        manager.add_user(name, email)
        print()
      elif choice == 2:
        manager.view_users()
        print()
      elif choice == 3:
        if not manager.users:
          print("No users to delete")
          continue
        manager.view_users()
        try:
          user_id = int(input("Enter id: "))
          if user_id < 1:
            print("Invalid id")
            continue
          manager.delete_user(user_id)
          print()
        except ValueError:
          print("Invalid id")
          continue
      elif choice == 4:
        print("Exiting...")
        break
    except ValueError:
      print("Invalid action")
      continue
      
if __name__ == "__main__":
  main()
