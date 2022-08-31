from Employee import Employee


class Director(Employee):
    count = 0;

    def __init__(self, name, salary, social_credits):
        super().__init__(name, salary)
        self.social_credits = social_credits

    def set_social_credits(self):
        print("enter social_credits:")
        self.social_credits = int(input())



    def get_social_credits(self):
        return self.social_credits;



    def show(self):
        super(Director, self).show()
        print(" Director\'s social_credits - ", self.social_credits);