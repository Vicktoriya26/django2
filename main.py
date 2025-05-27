import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_2.settings")

django.setup()

from shedult.models import Class, Student, Subject, Teacher

work = True
while work:
    print("""
        1.Додати предмет
        2.Додати вчителя
        3.Додати клас
        4.Додати учня
        0.Зупинити
    """)
    chois = int(input("вибери дію: "))
    if chois == 0:
        work = False

    if chois == 1:
        name = input("Назва предмету: ")
        description = input("Опис...")

        subject_db = Subject.objects.filter(name=name).first()

        if subject_db:
            print("Предмет уже існує!")
        else:
            new_subject = Subject(name=name, description=description)
            new_subject.save()


    if chois == 2:
        name = input("Ім'я: ")
        last_name = input("Призвіще: ")
        subject = input("Назва предмету: ")

        subject_db = Subject.objects.filter(name=subject).first()

        if subject_db:
            new_teacher = Teacher(name=name, last_name=last_name, subject=subject_db)
            new_teacher.save()
        else:
            print("Предмет не знайдено!")


    if chois == 3:
        name = input("Ім'я: ")
        year = input("Рік: ")
        

        class_db = Class.objects.filter(name=name).first()

        if class_db:
            print("Уже існує!")
        else:
            new_class = Class(name=name, year=year)
            new_class.save()



    if chois == 4:
        name = input("Ім'я: ")
        last_name = input("Призвіще: ")
        st_class = input("Назва класу: ")

        class_db = Class.objects.filter(name=st_class).first()

        if class_db:
            new_teacher = Student(name=name, last_ame=last_name, st_class=class_db)
            new_teacher.save()
        else:
            print("Нема!")
            

