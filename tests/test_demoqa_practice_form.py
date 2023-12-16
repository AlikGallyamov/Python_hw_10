import os
from selene import browser, have, be

from Python_hw_10.pages.registration_page import RegistrationPage
from Python_hw_10.resources.data_user import DataUser
from Python_hw_10.resources.path import CURRENT_DIR


def test_fill_form(browser_config):
    registration_page = RegistrationPage()
    dataUser = DataUser()

    registration_page.open_url('/automation-practice-form')

    registration_page.fill_first_name(dataUser.firstName)

    registration_page.fill_last_name(dataUser.lastName)

    registration_page.fill_email(dataUser.email)

    registration_page.choice_gender()

    registration_page.fill_number_phone(dataUser.numberPhone)

    registration_page.choice_birthday(dataUser.birthday)

    registration_page.fill_subject(dataUser.subjects)

    registration_page.choice_hobbies()

    registration_page.upload_img(CURRENT_DIR, 'img.png')

    registration_page.fill_address(dataUser.address)

    registration_page.state_city(dataUser.stateCity[0], dataUser.stateCity[1])

    registration_page.click_submit()

    registration_page.should_have_registered('Ivan', 'Ivanov', 'name@example.com', 'Male',  '8999999999',
                                             '22 February,1996', 'English', 'Sports, Reading, Music', 'img.png',
                                             'Baker Street', 'Haryana Panipat')
