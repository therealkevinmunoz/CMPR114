class Students:
    def GetInformation(self):
        print(f'Student last name is {self.last_name}')
        print(f'Student first name is {self.first_name}')
        print(f'Student address is {self.address}')
        print(f'Student city is {self.city}')
        print(f'Student state is {self.state}')
        print(f'Student zip code is {self.zipcode}')

Student3 = Students()

Student3.last_name = 'Munoz'
Student3.first_name = 'Kevin'
Student3.address = '1201 N Mountain View'
Student3.city = 'Santa Ana'
Student3.state = 'CA'
Student3.zipcode = '92703'

Student3.GetInformation()