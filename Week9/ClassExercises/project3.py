class PI:
    def GetInformation(self, LN, FN, Age, Address, City, State, Zipcode):
        return LN + ', ' + FN + ' ' + Age + ' ' + Address + ' ' + City + ', ' + State + ', ' + Zipcode

PersonalInformation = PI()
PersonalInformation.LastName = input('Enter your last name: ') 
PersonalInformation.FirstName = input('Enter your first name: ') 
PersonalInformation.Age = input('Enter your age: ') 
PersonalInformation.Address = input('Enter your address: ') 
PersonalInformation.City = input('Enter your city: ') 
PersonalInformation.State = input('Enter your state: ') 
PersonalInformation.Zipcode = input('Enter your zipcode: ')

print(PersonalInformation.GetInformation(PersonalInformation.LastName, PersonalInformation.FirstName, PersonalInformation.Age, PersonalInformation.Address, PersonalInformation.City, PersonalInformation.State, PersonalInformation.Zipcode))