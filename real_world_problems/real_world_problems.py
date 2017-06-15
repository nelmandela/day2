class University:
    def __init__(self, name):
        pass

class Student:
    def __init__(self, name, gender, reg_no):
        self.__name = name
        self.gender = gender
        self.reg_no = reg_no

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
class Undergraduate:
    def __init__(self, course_name, num_of_units, duration):
        self.course_name = course_name
        self.num_of_units = num_of_units 
        self.duration = duration
        self.completed_units = 0

    def graduate(self):
        if self.completed_units == self.num_of_units:
            return True
        else:
            return False

class Postgraduate(Undergraduate):
    def __init__(self, course_name, num_of_units, duration):
        super().__init__(course_name, num_of_units, duration)
        self.thesis = None

    def graduate(self, thesis):
        if self.completed_units == self.num_of_units and thesis is not None:
            return True
        else:
            return False


