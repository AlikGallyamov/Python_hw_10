from selene import browser, be, have
import os
from Python_hw_10.resources.path import CURRENT_DIR


class RegistrationPage:

    def open_url(self):
        browser.open('/automation-practice-form')

    def register(self, dataUser):
        browser.element('#firstName').click().should(be.blank).type(dataUser.firstName)

        browser.element('#lastName').click().should(be.blank).type(dataUser.lastName)

        browser.element('#userEmail').click().should(be.blank).type(dataUser.email)

        browser.element('[for="gender-radio-1"]').click()

        browser.element('#userNumber').click().should(be.blank).type(dataUser.phoneNumber)

        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1996"]').click()
        browser.element('[class*=month-select]').click()
        browser.element('[class*=month-select] [value="1"]').click()
        browser.element('[class*=day--022]').click()

        browser.element('#subjectsInput').click().type(dataUser.subject).press_tab()

        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

        browser.element('[type=file]').send_keys(os.path.join(CURRENT_DIR, dataUser.fileName))

        browser.element('#currentAddress').click().should(be.blank).type(dataUser.address)

        browser.element('#react-select-3-input').type(dataUser.state).press_enter()
        browser.element('#react-select-4-input').type(dataUser.city).press_enter()

        browser.element('#submit').press_enter()

    def should_have_registered(self, dataUser):
        browser.all('tbody tr td').should(
            have.texts('Student Name', f'{dataUser.firstName} {dataUser.lastName}', 'Student Email', dataUser.email,
                       'Gender',
                       dataUser.gender, 'Mobile',
                       dataUser.phoneNumber, 'Date of Birth', dataUser.dateBirth, 'Subjects', dataUser.subject,
                       'Hobbies', dataUser.hobbies, 'Picture', dataUser.fileName, 'Address', dataUser.address,
                       'State and City', f'{dataUser.state} {dataUser.city}'))
