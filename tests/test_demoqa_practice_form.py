import os
from selene import browser, have, be

from Python_hw_10.pages.registration_page import RegistrationPage
from Python_hw_10.resources.path import CURRENT_DIR


def test_fill_form(browser_config):
    registration_page = RegistrationPage()

    registration_page.open_url('/automation-practice-form')

    registration_page.fill_first_name('Ivan')

    registration_page.fill_last_name('Ivanov')

    registration_page.fill_email('name@example.com')

    registration_page.choice_gender()

    registration_page.fill_number_phone('8999999999')

    registration_page.choice_birthday()

    registration_page.fill_subject('English')

    registration_page.choice_hobbies()

    registration_page.upload_img(CURRENT_DIR, 'img.png')

    registration_page.fill_address('Baker Street')

    registration_page.state_city('Haryana', 'Panipat')

    registration_page.click_submit()

    registration_page.should_have_registered('Ivan', 'Ivanov', 'name@example.com', 'Male',  '8999999999',
                                             '22 February,1996', 'English', 'Sports, Reading, Music', 'img.png',
                                             'Baker Street', 'Haryana Panipat')
