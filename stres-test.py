
result = 0
arg = []
name = input('Ведите иммя: ')
def questions():
    qw = arg.append(input('Вы любите путешествовать - да, нет, точно да, точно нет: '))
    qw = arg.append(input('Вы любите ходить на природу - да, нет,  не знаю: '))
    qw = arg.append(input('Вы часто просиживаете вечер перед TV - часто, не часто, постоянно: '))
    qw = arg.append(input('Вы высыпаетесь - да, нет, иногда: '))
    qw = arg.append(input('Вы начинаете день без кофе - да, нет, не могу без кофе: '))
questions()


def Test(arg):
    global result
    for i in arg:
        if i == 'да':
            result += 2
        elif i == 'нет':
            result -= 1
        elif i == 'точно да':
            result += 2
        elif i == 'точно нет':
            result -= 2
        elif i == 'не могу без кофе':
            result -= 4
        elif i == 'не знаю':
            result += 0
        elif i == 'конечно':
            result += 3
        elif i == 'иногда':
            result += 1
        elif i == 'часто':
            result -= 1
        elif i == 'не часто':
            result +=1
        elif i == 'постоянно':
            result -= 2
        else:
            print('Вот не задача, в ответе был не верный выбор, начните пожалуйста сначала')
            answer = input('Начать заново - да, нет: ')
            if answer == 'да':
                return questions()
            else:
                print('Тест завершон!')
                break
Test(arg)

def analiz(result):
    if result <= 0:
        global finish
        global finish2
        finish = ('Есть видимые стресовые последствия,сотруднику необходим отпуск')
        print ('Ваш уровень стресоустойчивости', result,'Вам нужен отдых')
        result = finish
    elif result > 0:
        print ('Продолжайте в том же духе! Ваш уровень стресоустойчивости', result)
        finish2 = ('От роботы дохнут кони, а этот безсмертный пони')
        result = finish2
analiz(result)

def save_user():
    done = 'Тест завершён'
    with open('user.txt', 'a') as f:
        try:
            for line in str(name), finish:
                f.write(line + '\n')
        except:
            for line in str(name), finish2:
                f.write(line + '\n')
        print (done)
save_user()



