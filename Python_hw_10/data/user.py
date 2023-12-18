import dataclasses


@dataclasses.dataclass
class DataUser:
    firstName: str
    lastName: str
    email: str
    gender: str
    phoneNumber: str
    dateBirth: str
    fileName: str
    subject: str
    state: str
    city: str
    hobbies: str
    address: str
    fileName: str


dataUser = DataUser(firstName='Ivan', lastName='Ivanov', email='name@example.com', gender='Female',
                    phoneNumber='8999999999', dateBirth='03 December,2003', fileName='img.png', subject='English',
                    hobbies='Sports, Reading, Music', state='Haryana', city='Panipat', address='Baker Street')
