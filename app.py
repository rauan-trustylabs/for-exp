class User():
    def __init__(self, first_name, last_name, age, city ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def name_is_user(self):
        print(self.first_name + ' ' +
              self.last_name + ' ' +
              str(self.age) + ' ' + self.city)

    def greet_user(self):
        print(self.first_name, " HELLO ")

my_name = User("Dariga", "Raikhanova", 19, "Almaty" )

my_name.name_is_user()
my_name.greet_user()

class Privelegius():
    def __init__(self, privelegiu_for_resolution_add = "разрешено добавлять сообщения",
                 privelegiu_for_resolution_delete = "разрешено удалять пользователей",
                 privelegiu_for_resolution_ban = "разрешено банить пользователей"):
        self.privelegiu_for_resolution_add = privelegiu_for_resolution_add
        self.privelegiu_for_resolution_delete = privelegiu_for_resolution_delete
        self.privelegiu_for_resolution_ban = privelegiu_for_resolution_ban

    def privelegiu_for_people_add(self):
        print(self.privelegiu_for_resolution_add)

    def privelegiu_for_people_delete(self):
        print(self.privelegiu_for_people_delete)

    def privelegiu_for_people_ban(self):
        print(self.privelegiu_for_resolution_ban)


my_privelegiu = Privelegius()

my_privelegiu.privelegiu_for_people_add()
my_privelegiu.privelegiu_for_people_delete()
my_privelegiu.privelegiu_for_people_ban()






class Admin(User):
    def __init__(self,first_name, last_name, age, city):
        super().__init__( first_name, last_name, age, city)
        self.privelegius = ["разрешено добавлять сообщения", "разрешено удалять пользователей ",
                            "разрешено банить пользователей"]

    def show_privelegius(self):
        print(self.privelegius, " вот так вот")



your_name = Admin("", "", "", "")

your_name.show_privelegius()






