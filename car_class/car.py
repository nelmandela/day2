class Car:
    def __init__(self, name='General', model='GM' ,car_type='honda' ):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        if self.car_type == 'Porshe or Koenigsegg':
            self.num_of_wheels = 2
        else:
            self.num_of_wheels = 4

    def drive(self, spd):
        if self.car_type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self

    def wheels(self, num_of_wheels):
        return num_of_wheels


    def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
            return True