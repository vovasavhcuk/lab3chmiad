from Actor import Actor
from Employee import Employee
from Director import Director

if __name__ == '__main__':
    actor = Actor("gay", 100, "gaylord", "gaylords adventures")
    director = Director("Boss", 2000, 500)
    actor.show()
    actor.set_name();
    actor.set_film();
    actor.set_role();
    actor.set_salary();
    actor.show()
    director.show()




