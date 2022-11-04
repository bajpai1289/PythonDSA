# first something about classes
class User:
    def __init__(self, *args):
        self.username=args[0]
        self.name=args[1]
        self.email=args[2]
        print('User created')
    
    def introduceYourself(self,guest):
        print(f"hello {guest} you can call me {self.name}")
    
    def __repr__(self) -> str:
        return "User(username)='{}', name='{}', email='{}'".format(self.username,self.name,self.email)
    
    def __str__(self) -> str:
        return self.__repr__()
    
# user1=User('john','J ogn Doe','john@doe.com')
# user2=User('jane','Jane Doe','jane@doe.com')
# user2 .introduceYourself('David')
# print(user1)


# code for basic CRUD operations
class UserDatabase:
    def __init__(self) -> None:
        self.users=[]
    def insert(self,user):
        i=0
        while i<len(self.users):
            if self.users[i].username>user.username:
                break
            i+=1
        self.users.insert(i,user)
    def find(self, username):
        for user in self.users:
            if user.username==username:
                return user
            else: return 'Not found'
        
    def update(self,user):
        target = self.find(user.username)
        target.name,target.email=user.name, user.email
    
    def list_all(self):
        return self.users
      
        