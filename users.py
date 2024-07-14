class User():
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        self.access_level = 'user'

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_access_level(self):
        return self.access_level
    def set_name(self,name):
        self.__name = name
    def set_access_level(self,level):
        self.access_level = level

class Admin(User):
    def __init__(self,id,name):
        super().__init__(id,name)
        self.__access_level_admin = 'admin'
    def add_user(self,user_list,user):
        if isinstance(user,User):
            flag = True
            for us in user_list:
                 if us.get_id() == user.get_id():
                    flag = False
                    break
            if flag:
                user_list.append(user)
                print("User added successfully")
            else:
                print("User already exists")
        else:
            print("Invalid user")
    def remove_user(self,user_list,user):
         if isinstance(user,User):
             for i in range(len(user_list)):
                 if user_list[i].get_id() == user.get_id():
                     user_list.pop(i)
                     print("User removed successfully")
                     break
             else:
                 print("User not found")


users=[]
user1=User(1,"Alex")
user2=User(2,"Boris")
user3=Admin(3,"Greg")
user3.add_user(users,user1)
user3.add_user(users,user2)
user3.add_user(users,user3)
user3.remove_user(users,user2)
for user in users:
    print(f"ID: {user.get_id()}, Name: {user.get_name()}")