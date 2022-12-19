import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tkinter import messagebox, simpledialog
import time, json, re
from sys import platform

if platform == "linux" or platform == "linux2":
    chrome_path = './drivers/chromedriver'

elif platform == "darwin":
    chrome_path = './drivers/chromedriver_mac'

options = Options()
options.add_argument('user-data-dir=/tmp/tarun')

class ObtainInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        self.driver.maximize_window()
        self.driver.get('https://ofertadecursos.uniandes.edu.co/')
        self.driver.implicitly_wait(10)
    def test_main(self):
        # ask the user for the fiename

        # filename = simpledialog.askstring("Input", "Ingrese el nombre del archivo que contiene las materias")
        filename = 'prueba.txt'
        # Load the course list from the folder input
        with open('input/'+filename) as file:
            courses = file.readlines()
        # Remove whitespace characters like `\n` at the end of each line
        courses = [x.strip() for x in courses]
        driver = self.driver
        #show a message box to ask the user to check captcha
        messagebox.showinfo('Captcha', 'Por favor, ingrese el captcha y presione OK')

        #get the nrc-input element
        nrc_input = driver.find_element(By.ID, 'nrc')

        # get the button to search
        search_button = driver.find_element(By.XPATH, '//*[@id="sidebar-wrapper"]/div[2]/form/button[3]')

        courses_info = {}
        # Loop through the courses
        for course in courses:
            nrc_input.clear()
            nrc_input.send_keys(course)
            search_button.click()
            # wait for the page to load
            time.sleep(2)
            # get the list of divs that contain the course info
            page_info = driver.find_elements(By.CSS_SELECTOR, '#wrapper > div.page-content-wrapper > div > div.card')
            # get the first div
            course_info = page_info[0]
            # get the course title
            course_nrc_name = course_info.find_element(By.CSS_SELECTOR, '.card-header-title b').text

            # get the course name
            course_name = course_nrc_name[10:]

            # iterate through the page info to get the course schedule, teacher, nrc, etc. to save it in a file
            for info in page_info:
                section_col = info.find_element(By.CSS_SELECTOR, '.card-header .row .col-md-3:nth-child(1)').text
                # from the section column, get the cupo, nrc, seccion, creditos. using regex
                print(course_name)
                # print(section_col)
                pattern = r'Cupo:\s+(\d+)\s+NRC:\s+(\d+)\s+Sección:\s+(\d+)\s+Créditos:\s+(\d+)'

                match = re.search(pattern, section_col)
                if match:
                    cupo = match.group(1)
                    nrc = match.group(2)
                    seccion = match.group(3)
                    creditos = match.group(4)
                    print(f'Cupo: {cupo}, NRC: {nrc}, Sección: {seccion}, Créditos: {creditos}')
                else:
                    print('Match not found')

                teacher_col = info.find_element(By.CSS_SELECTOR, '.card-header .row .col-md-3:nth-child(2)').text
                # from the teacher column, get the teacher name using regex
                pattern = r'Instructor principal:\s+(.+?)\s+Campus:'
                # print(teacher_col)
                match = re.search(pattern, teacher_col)
                if match:
                    teacher = match.group(1)
                    print(f'Instructor: {teacher}')
                else:
                    print('Match not found')
                schedule_col = info.find_element(By.CSS_SELECTOR, '.card-header .row .col-md-6')
                # from the schedule column, get the schedule
                schedule_rows = schedule_col.find_elements(By.CSS_SELECTOR, '.table > tbody tr')
                schedule_list = []
                for row in schedule_rows:
                    # get the schedule
                    # print(row.text)
                    schedule_days = row.find_element(By.CSS_SELECTOR, 'th').text
                    # print(schedule_days)
                    schedule_time = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
                    # print(schedule_time)
                    schedule_room = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
                    # print(schedule_room)
                    schedule_actual = {'days': schedule_days, 'time': schedule_time, 'room': schedule_room}
                    print(schedule_actual)
                    schedule_list.append(schedule_actual)
                # save the info in a file
                actual_dict = courses_info.get(course, {})
                actual_dict[nrc] = {'cupo': cupo, 'seccion': seccion, 'creditos': creditos, 'teacher': teacher, 'schedule': schedule_list}
                courses_info[course] = actual_dict
        # save the info in a json file
        with open('output/'+filename[:-4]+'.json', 'w') as outfile:
            json.dump(courses_info, outfile)
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_prueba'))