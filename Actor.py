from Employee import Employee


class Actor(Employee):
    count = 0;

    def __init__(self, name, salary, role, film):
        super().__init__(name, salary)
        self.role = role
        self.film = film

    def set_role(self):
        print("enter role:")
        self.role = str(input())

    def set_film(self):
        print("enter film:")
        self.film = str(input())


    def get_role(self):
        return self.name;

    def get_film(self):
        return self.film;

    def show(self):
        super(Actor, self).show()
        print("Role - ", self.role, "\nFilm - ", self.film);