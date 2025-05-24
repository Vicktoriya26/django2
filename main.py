import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_2.settings")

django.setup()

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
        