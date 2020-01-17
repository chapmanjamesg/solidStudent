class Student():
    # def __init__(self):



    @property # the getter
    def first_name(self):
        try:
            return self.__first_name 
        except AttributeError:
            return ""

    @first_name.setter # the setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string for a first name")


    @property # the getter
    def last_name(self):
        try:
            return self.__last_name 
        except AttributeError:
            return ""

    @last_name.setter # the setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string for a last name")


    @property # the getter
    def age(self):
        try:
            return self.__age 
        except AttributeError:
            return 0

    @age.setter # the setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide a integer for a age")


    @property # the getter
    def cohort_number(self):
        try:
            return self.__cohort_number 
        except AttributeError:
            return 0

    @cohort_number.setter # the setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError("Please provide a integer for a cohort number")

    @property # the getter
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except AttributeError:
            return ""



l = Student()
l.first_name = "james"
l.last_name = "chapman"
l.age = 33
l.cohort_number= 36

l.first_name = "terry"

print(l.full_name)

