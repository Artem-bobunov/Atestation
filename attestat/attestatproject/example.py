
import os
import csv
import os
import pandas as pd
path = '/home/avbobunov@vbti.local/Desktop/Аттестация/Отдел пространственных данных и информационного взаимодействия/ans.csv'
with open(path, "r") as f:
    reader = csv.reader(f)
    c = 0
    c1 = 0
    array = []
    for row in reader:
        print(row[0],'yyy')

        for sr in reader:
            #print(sr[1])
            if row[1] == sr[1]:
                print(row[0],'==',sr[0])
            break





#otd = {'07': ['AlexeyAB', 'AlexandrovAA'],
                #'05': ['olya', 'yulia']}
#s = None
#for key,value in otd.items():
#    for v in value:
#        if v == fio:
#            s = key
            #print(key)
#print(s)

#print(commands_list['func1'])
"""for key,value in commands_list.items():
  print(key)
  for v in value:
      print(v)

import random
#print(random.choice(list(commands_list.items())))

 m = []
            ida = a.values_list('id',flat = True)
            #print(ida)

            #Достаем id вопрос, если id

            #Достаем id ответов
            s = []
            sd = []
            dictonary = {}
            id_ans = None
            id_qus = Question.objects.filter(id_departament__in=str(id_dep))
            key = id_qus
            arr = []
            for k in key:
                arr.append(k)
            print(arr)

            for i in ida:
                id_ans = Answer.objects.filter(quest__in=str(i)).values_list('answers',flat=True)
                print(id_ans)
            dictonary.setdefault(key, [v for v in id_ans])
            print(dictonary)"""