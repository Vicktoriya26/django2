from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_ame = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_ame = models.CharField(max_length=100)
    st_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    DAYS = (
        ('Monday', 'Понеділок'),
        ('Tuesday', 'Вівторок' ),
        ('Wednesday', 'Середа'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятния'),
        ('Saturday', 'Субота'),
        ('Sunday', 'Неділя')
    )

    week_day = models.CharField(max_length=20)
    start_time = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    st_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"день: {self.week_day} Початок уроку: (self.start_time) Предмет: (self.subject)"
    

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True)


















