from database import Database
from admin import Admin
from user import User
from saveable import Saveable

a = Admin('paco', 'perez', 2)
b = Admin('rolf', 'smith', 1)

a.save()
b.save()

user = Database.find(lambda x: x['username'] == 'paco')[0]
user_obj = Admin(**user)
print(user_obj.username)

print(isinstance(user_obj, Saveable))

users_to_save = [a, b, User('jose', '1234')]
for u in users_to_save:
    u.save()
    