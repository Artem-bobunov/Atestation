from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Question, Answer,Departament,Result,Atchet
import random
import numpy as np
import docxtpl
from random import randint
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from datetime import datetime

# Create your views here.
def greetin(request):
    return render(request,'greetings.html')

#Номер отдела содержит список сотрудников
# 
@cache_page(1 * 1)
def listObjects(request):
    
    last_name = request.user.last_name
    first_name = request.user.first_name
    
    otd = {
           '99': ['FedotovaMN','VedeneevaEV','GolybevaJN','ShishkinaAA',
           'PetrychinVI','SylimovAS','KolpakovaNA','ShalkovaNN',
           'RebrinaGV','MyrovaLV','RomashkinaIM',
           'KrasnovDV','ZiatikovaVV','PopovaTV','MazlovaLV',
           'SergeevaOI','CishenkoEN','EgorovaLV','LoginovaNA'],
            '11':['ManyshkinaJA'],

           }
    usr = request.user
    #print(usr)
    #search_usr = Departament.objects.get(author = usr)
    dslv = {}
    dslv1 = {}
    dslv2 = {}
    dslv3 = {}
    dep =None
    cat =None
    cat1 =None
    cat2 =None
    cat3 =None
    tb = 0
    tb1 = 0
    tb2 = 0
    tb3 = 0
    total = 0
    total_score = []
    total_score1 = []
    total_score2 = []
    total_score3 = []
    search_usr = None
    #Вытаскиваем номер отдела
    for t, y in otd.items():
        #print(t)
        for v in y:
            #print(v)
            if v in str(usr):
                search_usr = t
    #print(search_usr)


    #Вытаскиваем название отдела
    dep = Departament.objects.get(numberDep=str(search_usr)).departaments
    #print(dep)
    #Вытаскиваем ID_User_Dep в таблице Отдела
    id_dep_user = Departament.objects.get(numberDep=search_usr).ID_User_Dep
    # print(id_dep_user)

    #id_dep = search_usr.id
    #Считаем какое количество id_departament есть в таблице Вопросов
    a = Question.objects.filter(id_departament = str(id_dep_user))
    #print(a)
    #Количество айди отделов в таблице вопросов
    counts = a.count()
    #print(a)
    #print(counts)

    for i in a:
        cat = i.category
        if cat=='Обычный':
            #Достаем сам вопрос
            quest0 = i.questions
            #Достаем айди вопроса
            id_qeus = i.id
            #Обращаемся к таблице ответов и ищем где будет Id_вопроса равен id в таблице вопросов
            id_ans = Answer.objects.filter(quest=id_qeus)
            #Создаем массив для ответов
            value = []
            for v in id_ans:
                value.append(v.answers)
            #print(value)
            dslv.setdefault(quest0,value)
    #print('Me')


    #print(dslv)

    #Достаем вопросы по делопроизводству
    for c in a:
        #Смотрим категорию и если она равна  по кадастровому законодательству
        cat1 = c.category
        #print(cat)
        if cat1 == 'по делопроизводству':
            #print('Зашли')
            #print(cat)
            # Достаем сам вопрос
            quest1 = c.questions
            #print(quest1)
            # Достаем айди вопроса
            id_qeus1 = c.id
            #print(id_qeus1)
            # Обращаемся к таблице ответов и ищем где будет Id_вопроса равен id в таблице вопросов
            id_ans1 = Answer.objects.filter(quest=id_qeus1)
            #print(id_ans1)
            value1 = []
            for b in id_ans1:
                value1.append(b.answers)
            #print(quest1,value1)
            dslv1.setdefault(quest1, value1)
            #print(dslv1)

    # Достаем вопросы по делопроизводству
    for c1 in a:
        # Смотрим категорию и если она равна  по кадастровому законодательству
        cat2 = c1.category
        #print(cat2)
        if cat2 == 'по охране труда':
            #print('Зашли1')
            # print(cat)
            # Достаем сам вопрос
            quest2 = c1.questions
            # print(quest1)
            # Достаем айди вопроса
            id_qeus2 = c1.id
            # print(id_qeus1)
            # Обращаемся к таблице ответов и ищем где будет Id_вопроса равен id в таблице вопросов
            id_ans2 = Answer.objects.filter(quest=id_qeus2)
            # print(id_ans1)
            value2 = []
            for b1 in id_ans2:
                value2.append(b1.answers)
            # print(quest1,value1)
            dslv2.setdefault(quest2, value2)
            #print(dslv2)

    #Достаем вопросы по делопроизводству
    for c2 in a:
        # Смотрим категорию и если она равна  по кадастровому законодательству
        cat3 = c2.category
        #print(cat3)
        if cat3 == 'по трудовому законодательству':
            #print('Зашли3')
            # print(cat)
            # Достаем сам вопрос
            quest3 = c2.questions
            # print(quest1)
            # Достаем айди вопроса
            id_qeus3 = c2.id
            # print(id_qeus1)
            # Обращаемся к таблице ответов и ищем где будет Id_вопроса равен id в таблице вопросов
            id_ans3 = Answer.objects.filter(quest=id_qeus3)
            # print(id_ans1)
            value3 = []
            for b2 in id_ans3:
                value3.append(b2.answers)
            # print(quest1,value1)
            dslv3.setdefault(quest3, value3)
            #print(dslv3)



    dslv = dict(random.sample(dslv.items(), 15))
    dslv1 = dict(random.sample(dslv1.items(),5))
    dslv2 = dict(random.sample(dslv2.items(),5))
    dslv3 = dict(random.sample(dslv3.items(),5))
    #print(dslv1)


    if request.method == 'POST':
        
        res_dslv ={}
        res_dslv1 ={}
        res_dslv2 ={}
        res_dslv3 ={}
        

        print('Метод выполнился')

        try_ques = None
        try_ques1 = None
        try_ques2 = None
        try_ques3 = None

        res1 = {}
        res2 = {}
        res3 = {}
        res4 = {}
        
        get_check = request.POST.getlist('check')
        # Достаем ответы по кадровому законодательству
        get_check1 = request.POST.getlist('check1')

        get_check2 = request.POST.getlist('check2')
        get_check3 = request.POST.getlist('check3')

        get_ques = request.POST.getlist('keys')
        print(get_ques)
        qtqs = []
        check_arr = []
        for n in get_ques:
            qtqs.append(n)
        for c in get_check:
            check_arr.append(c)
        keys = np.array(get_ques)
        values = np.array(get_check)

        for A, B in zip(keys, values):
            res1.setdefault(A,B)
        for k,v in res1.items():
            d0 = Departament.objects.get(departaments=dep).ID_User_Dep
            q = Question.objects.filter(id_departament=d0).get(questions=k).id
            ct = Question.objects.filter(id_departament=d0).get(questions=k).category
            res_ans = Answer.objects.filter(quest=q).get(ball='1').answers
            #print(q)
            #print(k)
            #print(v)
            bl = Answer.objects.filter(quest=q).get(answers=v).ball
            if bl == '1':
                total_score.append(int(bl))
            tb = sum(total_score)
            #print(total_score)
            res_dslv.setdefault(k,[v, res_ans])
            
            res_db = Result()
            res_db.departament = dep
            res_db.users = usr
            res_db.questions = k
            res_db.category = ct
            res_db.select_answers = v
            res_db.good_answers = res_ans
            res_db.result_balls = bl
            res_db.save()
            



        #print(res1)
        get_ques1 = request.POST.getlist('keys1', default=None)
        qtqs1 = []
        check_arr1 = []
        for n1 in get_ques1:
            qtqs1.append(n1)
        for c1 in get_check1:
            check_arr1.append(c1)
        keys1 = np.array(get_ques1)
        values1 = np.array(get_check1)

        for A1, B1 in zip(keys1, values1):
            res2.setdefault(A1,B1)
        for k1,v1 in res2.items():
            #print(k1)
            d = Departament.objects.get(departaments=dep).ID_User_Dep
            #print(d)
            q1 = Question.objects.filter(id_departament=d).get(questions=k1).id
            ct1 = Question.objects.filter(id_departament=d).get(questions=k1).category
            res_ans1 = Answer.objects.filter(quest=q1).get(ball='1').answers
            bl1 = Answer.objects.filter(quest=q1).get(answers=v1).ball
            if bl1 == '1':
                total_score1.append(int(bl1))
            tb1 = sum(total_score1)
            #print(tb1)
            res_dslv1.setdefault(k1,[v1, res_ans1])
            
            res_db1 = Result()
            res_db1.departament = dep
            res_db1.users = usr
            res_db1.questions = k1
            res_db1.category = ct1
            res_db1.select_answers = v1
            res_db1.good_answers = res_ans1
            res_db1.result_balls = bl1
            res_db1.save()


        get_ques2 = request.POST.getlist('keys2', default=None)
        qtqs2 = []
        check_arr2 = []
        for n2 in get_ques2:
            qtqs2.append(n2)
        for c2 in get_check2:
            check_arr2.append(c2)
        keys2 = np.array(get_ques2)
        values2 = np.array(get_check2)
        for A2, B2 in zip(keys2, values2):
            res3.setdefault(A2,B2)
        for k2,v2 in res3.items():
            d1 = Departament.objects.get(departaments=dep).ID_User_Dep
            q2 = Question.objects.filter(id_departament=d1).get(questions=k2).id
            ct2 = Question.objects.filter(id_departament=d1).get(questions=k2).category
            res_ans2 = Answer.objects.filter(quest=q2).get(ball='1').answers
            bl2 = Answer.objects.filter(quest=q2).get(answers=v2).ball
            if bl2 == '1':
                total_score2.append(int(bl2))
            tb2 = sum(total_score2)
            res_dslv2.setdefault(k2,[v2, res_ans2])
            
            res_db2 = Result()
            res_db2.departament = dep
            res_db2.users = usr
            res_db2.questions = k2
            res_db2.category = ct2
            res_db2.select_answers = v2
            res_db2.good_answers = res_ans2
            res_db2.result_balls = bl2
            res_db2.save()

        get_ques3 = request.POST.getlist('keys3', default=None)
        qtqs3 = []
        check_arr3 = []
        for n3 in get_ques3:
            qtqs3.append(n3)
        for c3 in get_check3:
            check_arr3.append(c3)
        keys3 = np.array(get_ques3)
        values3 = np.array(get_check3)
        for A3, B3 in zip(keys3, values3):
            res4.setdefault(A3,B3)
        for k3,v3 in res4.items():
            d2 = Departament.objects.get(departaments=dep).ID_User_Dep
            q3 = Question.objects.filter(id_departament=d2).get(questions=k3).id
            ct3 = Question.objects.filter(id_departament=d2).get(questions=k3).category
            res_ans3 = Answer.objects.filter(quest=q3).get(ball='1').answers
            bl3 = Answer.objects.filter(quest=q3).get(answers=v3).ball
            if bl3 == '1':
                total_score3.append(int(bl3))
            tb3 = sum(total_score3)
            res_dslv3.setdefault(k3,[v3,res_ans3])
           
            res_db3 = Result()
            res_db3.departament = dep
            res_db3.users = usr
            res_db3.questions = k3
            res_db3.category = ct3
            res_db3.select_answers = v3
            res_db3.good_answers = res_ans3
            res_db3.result_balls = bl3
            res_db3.save()


        total = tb+tb1+tb2+tb3
        document = docxtpl.DocxTemplate('C:\\attestation\\attestat\\media\\Result.docx')
        res_attestation = None
        if total < 25:
            res_attestation = "Тестирование не пройдено!"
        if total > 24:
            res_attestation = "Тестирование пройдено!"
        context_doc = {'tb':tb,'tb1':tb1,'tb2':tb2,'tb3':tb3,'total':total,"last_name":last_name,"first_name":first_name,"dep":dep,"res_attestation":res_attestation,"res_dslv":res_dslv,"res_dslv1":res_dslv1,
                       "res_dslv2":res_dslv2,"res_dslv3":res_dslv3}
        document.render(context_doc)
        document.save('C:\\attestation\\attestat\\media\\'+ str(usr) + '.docx' )
        file_download = str(usr) + '.docx'
        
        
        itogi = Atchet()
        itogi.departament = dep
        itogi.users = str(last_name)+' '+str(first_name)
        itogi.result_balls = total
        if total < 25:
            itogi.res = 'Тестирование не пройдено!'
        if total > 24:
            itogi.res = 'Тестирование пройдено!'
        itogi.dt = datetime.now().strftime("%Y-%m-%d")
        itogi.save()
        return render(request,'result.html', context = {"total":total,"tb":tb, "tb1":tb1,"tb2":tb2,"tb3":tb3,"res_dslv":res_dslv,"res_dslv1":res_dslv1,"dep":dep,"usr": usr,
                                                        "res_dslv2":res_dslv2,"res_dslv3":res_dslv3,"last_name":last_name,"first_name":first_name,"file_download":file_download})



        #return render(request,'result.html')

    return render(request, 'list.html', context={"dictonary":dslv,"usr": usr, "dep": dep,"dictonary1":dslv1,"cat":cat,"dictonary2":dslv2,"dictonary3":dslv3,"last_name":last_name,"first_name":first_name})

def res_test(request):
    all_view = Atchet.objects.order_by('-dt')
    return render(request,'res_test.html',context = {'all_view':all_view})

def results(request):

    get_check=None
    print('Тут')
    if request.POST.get('res'):
        print('Метод выполнился')
        get_check = 'Результат'

    return render(request,'result.html',context = {"get_check":get_check})