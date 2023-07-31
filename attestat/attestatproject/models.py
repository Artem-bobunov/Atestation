from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Departament(models.Model):

    #Отделы
    dep = (
        ('Волгоградский производственный участок','Волгоградский производственный участок'),
        ('Отдел государственной кадастровой оценки земельного фонда','Отдел государственной кадастровой оценки земельного фонда'),
        ('Отдел государственной кадастровой оценки объектов капитального строительства','Отдел государственной кадастровой оценки объектов капитального строительства'),
        ('Отдел информационных технологий','Отдел информационных технологий'),
        ('Отдел кадровой работы и делопроизводства','Отдел кадровой работы и делопроизводства'),
        ('Отдел материально-технического обеспечения и государственных закупок','Отдел материально-технического обеспечения и государственных закупок'),
        ('Отдел пространственных данных и информационного взаимодействия','Отдел пространственных данных и информационного взаимодействия'),
        ('Отдел хранения и выдачи информации','Отдел хранения и выдачи информации'),
        ('Районные отделы','Районные отделы'),
        ('Секретарь','Секретарь'),
        ('Финансово-экономический отдел','Финансово-экономический отдел'),
        ('Юридический отдел','Юридический отдел'),
        ('Отдел материально-технического обеспечения','Отдел материально-технического обеспечения'),

    )

    departaments = models.CharField('Отдел',max_length=1000,null=True,blank=True,choices=dep)
    numberDep = models.CharField('Номер отдела',max_length=1000,null=True,blank=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    ID_User_Dep = models.IntegerField('Id_Пользователя_отдела',null=True,blank=True)
    #id_question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)

class Question(models.Model):
    ctg = (
        ('по делопроизводству','по делопроизводству'),
        ('Обычный','Обычный'),
        ('по охране труда','по охране труда'),
        ('по трудовому законодательству','по трудовому законодательству'),
    )
    questions = models.CharField('Вопрос', max_length=1000,null=True,blank=True)
    id_departament = models.ForeignKey(Departament, on_delete=models.CASCADE,null=True,blank=True)
    category = models.CharField('Категория', max_length=1000,null=True,blank=True, choices=ctg )

class Answer(models.Model):

    #Выборка для правильного ответа
    select_correct_answer = (
        ('0','0'),
        ('1','1'),
    )
    #Правильный бал
    result_ball = (
        ('0','0'),
        ('1','1'),
    )
    answers = models.CharField('Ответ на вопрос', max_length=1000, null=True, blank=True)
    quest = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    ball = models.CharField('Бал',null=True,blank=True,max_length=10,choices = select_correct_answer)
    #correct_answer = models.CharField('Правильный ответ',null=True,max_length=10,blank=True,choices = result_ball)

class Result(models.Model):
    departament = models.CharField('Отдел',max_length=1000,null=True,blank=True)
    users = models.CharField('Пользователь',max_length=1000,null=True,blank=True)
    questions = models.CharField('Вопрос',max_length=1000,null=True,blank=True)
    category = models.CharField('Категория',max_length=1000,null=True,blank=True)
    select_answers = models.CharField('Выбранный ответ',max_length=1000,null=True,blank=True)
    good_answers = models.CharField('Правильный ответ',max_length=1000,null=True,blank=True)
    result_balls = models.CharField('Балл',max_length=1000,null=True,blank=True)


class Atchet(models.Model):
    departament = models.CharField('Отдел',max_length=1000,null=True,blank=True)
    users = models.CharField('Пользователь',max_length=1000,null=True,blank=True)
    result_balls = models.CharField('Общий Балл', max_length=1000, null=True, blank=True)
    res = models.CharField('Результат Тестирования', max_length=1000, null=True, blank=True)
    dt = models.DateField('Дата прохождения', max_length=1000, null=True, blank=True)
