#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task4-11')
def task():
    pass
    #------- пишите код здесь -----
    def S(a,b):
        for stroka in range (1,a+1):
            for stolbec in range (1,b+1):
                r.pt()
                r.rt()
            r.dn()
            r.lt(b)
    r.rt()
    r.dn()
    S(3,6)
    r.rt(8)
    r.up(3)
    S(4,9)
    #------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
