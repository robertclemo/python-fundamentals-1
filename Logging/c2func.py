from c2class import Students
import time
import os
import datetime


def stuCredit():
    studentPrint=[]
    student=input("What is your name: ")
    try:
        gpa=float(input("What is your GPA: "))
        if gpa < 0 or gpa > 4.0:
            print ("\nGPA has to be between 0 and 4")
            time.sleep(2)
            os.system('clear')
            stuCredit()
    except ValueError:
        print("Sorry, not a resonable responds.")
        time.sleep(2)
        os.system('clear')
        stuCredit()
    credit=int(gpa*10)
    studentC=Students(student, gpa, credit)
    studentPrint.append(studentC)
    with open ("checkLog.txt", "a") as log:
        log.write('\n' + str(datetime.datetime.now()))
        log.write(f'\nStudent {studentC.student} checked there credit')
        log.close

    for studentC in studentPrint:
        time.sleep(2)
        os.system('clear')
        print(f'Hello {studentC.student}')
        print(f'Since, your GPA is {studentC.gpa}')
        if studentC.gpa >= 3.0:
            print(f'Congratulation your credit is ${studentC.credit} we hope you continue striving for excellence.')
        else:
            print(f'Your credit is ${studentC.credit}, please strive to elevate yourself further.')