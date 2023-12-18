from Python_hw_10.pages.registration_page import RegistrationPage
from Python_hw_10.resources.user import DataUser


def test_fill_form(browser_config):
    dataUser = DataUser(firstName='Ivan', lastName='Ivanov', email='name@example.com', gender='Female',
                        phoneNumber='8999999999', dateBirth='03 December,2003', fileName='img.png', subject='English',
                        hobbies='Sports, Reading, Music', state='Haryana', city='Panipat', address='Baker Street')
    registrationPage = RegistrationPage()
    registrationPage.open_url()
    registrationPage.register(dataUser)
    registrationPage.should_have_registered(dataUser)
