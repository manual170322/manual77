from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.utils.translation import ugettext as _
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.urls import reverse

from django.contrib.auth import login as auth_login

import time

# Подключение моделей
from .models import Category, Teststask, Question, Protocol, Decision
# Подключение форм
from .forms import CategoryForm, TeststaskForm, QuestionForm, DecisionForm, SignUpForm

# Create your views here.
# Групповые ограничения
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='403')

# Стартовая страница 
def index(request):
    return render(request, "index.html")

# Контакты
def contact(request):
    return render(request, "contact.html")

# Лекции
def lecture(request):
    return render(request, "lecture.html")

# Видеоуроки
def video(request):
    return render(request, "video.html")

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def category_index(request):
    category = Category.objects.all().order_by('title')
    return render(request, "category/index.html", {"category": category,})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def category_create(request):
    try:
        if request.method == "POST":
            category = Category()
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/create.html", {"form": categoryform})            
        else:        
            categoryform = CategoryForm(request.FILES)
            return render(request, "category/create.html", {"form": categoryform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Category.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Category.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def category_edit(request, id):
    try:
        category = Category.objects.get(id=id) 
        if request.method == "POST":
            category.title = request.POST.get("title")
            categoryform = CategoryForm(request.POST)
            if categoryform.is_valid():
                category.save()
                return HttpResponseRedirect(reverse('category_index'))
            else:
                return render(request, "category/edit.html", {"form": categoryform})            
        else:
            # Загрузка начальных данных
            categoryform = CategoryForm(initial={'title': category.title, })
            return render(request, "category/edit.html", {"form": categoryform})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def category_delete(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect(reverse('category_index'))
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
@group_required("Managers")
def category_read(request, id):
    try:
        category = Category.objects.get(id=id) 
        return render(request, "category/read.html", {"category": category})
    except Category.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def teststask_index(request):
    teststask = Teststask.objects.all().order_by('title')
    return render(request, "teststask/index.html", {"teststask": teststask,})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def teststask_create(request):
    try:
        if request.method == "POST":
            teststask = Teststask()
            teststask.title = request.POST.get("title")
            teststask.category = Category.objects.filter(id=request.POST.get("category")).first()
            teststask.details = request.POST.get("details")
            teststask.minutes = request.POST.get("minutes")
            teststask.limit = request.POST.get("limit")
            teststask.save()
            return HttpResponseRedirect(reverse('teststask_index'))
        else:        
            teststaskform = TeststaskForm(request.FILES)
            return render(request, "teststask/create.html", {"form": teststaskform})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Teststask.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Teststask.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def teststask_edit(request, id):
    try:
        teststask = Teststask.objects.get(id=id) 
        if request.method == "POST":
            teststask.title = request.POST.get("title")
            teststask.category = Category.objects.filter(id=request.POST.get("category")).first()
            teststask.details = request.POST.get("details")
            teststask.minutes = request.POST.get("minutes")
            teststask.limit = request.POST.get("limit")
            teststask.save()
            return HttpResponseRedirect(reverse('teststask_index'))
        else:
            # Загрузка начальных данных
            teststaskform = TeststaskForm(initial={'category': teststask.category, 'title': teststask.title,'details': teststask.details,'minutes': teststask.minutes,'limit': teststask.limit, })
            return render(request, "teststask/edit.html", {"form": teststaskform})
    except Teststask.DoesNotExist:
        return HttpResponseNotFound("<h2>Teststask not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def teststask_delete(request, id):
    try:
        teststask = Teststask.objects.get(id=id)
        teststask.delete()
        return HttpResponseRedirect(reverse('teststask_index'))
    except Teststask.DoesNotExist:
        return HttpResponseNotFound("<h2>Teststask not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
@group_required("Managers")
def teststask_read(request, id):
    try:
        teststask = Teststask.objects.get(id=id) 
        return render(request, "teststask/read.html", {"teststask": teststask})
    except Teststask.DoesNotExist:
        return HttpResponseNotFound("<h2>Teststask not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Список для выбора тестового задания
@login_required
def teststask_list(request):
    teststask = Teststask.objects.all().order_by('title')
    return render(request, "teststask/list.html", {"teststask": teststask,})

@login_required
def teststask_run(request, id):
    try:
        # Вопросы и ответы к тестовому заданию
        question = Question.objects.filter(teststask_id=id)
        # Порог в % и время на выполнение тестового задания в мин.
        teststask = Teststask.objects.get(id=id)
        teststask_title = teststask.title
        limit = teststask.limit
        minutes = teststask.minutes
        print(minutes)
        # Если нажата кнопка Accept (Принять)
        if ('accept_btn' in request.POST) or ('accept_timer_btn' in request.POST):
            # Считать со страницы ответы пользователя
            # {'radio6': 'on1', 'radio7': 'on2', 'cbox28': 'on2', 'cbox38': 'on3', 'radio9': 'on4', 'radio10': 'on5'}
            # 'radio7': 'on2' - для вопроса с id записи 7 выбрагн второй вариант ответа
            # 'cbox28': 'on2', 'cbox38': 'on3' - для вопроса с id записи 8 выбраны 2 и 3 варианты ответов
            dictionary_answer = {}
            for key, value in request.POST.items():
                if key != 'csrfmiddlewaretoken':
                    if key != 'accept_btn':
                        dictionary_answer.update({key:value})
                #print(f'Key: {key}')
                #print(f'Value: {value}')
            #for key in dictionary_answer:
                #print(key,dictionary_answer[key])
            #print(dictionary_answer)
            # Сгруппировать многовариантые ответы и привести в более понятный вид
            # {'radio6': 'on1', 'radio7': 'on2', 'cbox28': 'on2', 'cbox38': 'on3', 'radio9': 'on4', 'radio10': 'on5'}
            # в
            # {'6': '1', '7': '2', '8': '23', '9': '4', '10': '5'}
            answers = {}
            for key in dictionary_answer:
                question_id = key[5:len(key)]           # выделить id вопроса                    
                if key[0:5]=='radio':                   # У вопроса только один вариант ответа
                    answers.update({ question_id : dictionary_answer[key][2:3]})
                if key[0:4]=='cbox':                    # У вопроса может быть несколько вариантов ответов
                    total = ''                          # Ответы на вопрос в виде 134 (выбраны первый, третий и четвертый варианты ответов)
                    temp = dictionary_answer            # Для перебора всех ответов на вопрос с данным question_id 
                    for key in temp:
                        if key[5:len(key)] == question_id:
                            total = total + dictionary_answer[key][2:3]
                    answers.update({question_id : total})
            print(answers)
            # Считать из базы данных в словарь id вопроса и отметки о правильности ответов
            question2 = Question.objects.values('id', 'ok1', 'ok2', 'ok3', 'ok4', 'ok5').filter(teststask_id=id)
            dictionary_question = [entry for entry in question2]
            #print(dictionary_question)
            # Перебрать все вопросы и представить их в удобоваримом виде,
            # например пара 'id вопроса' : 'правильный ответ (ответы)'
            # {'6': '1', '7': '2', '8': '23', '9': '4', '10': '5'}
            questions = {}
            for d in dictionary_question:
                total = ''
                if d['ok1'] == True:
                    total = total + '1'
                if d['ok2'] == True:
                    total = total + '2'
                if d['ok3'] == True:
                    total = total + '3'
                if d['ok4'] == True:
                    total = total + '4'
                if d['ok5'] == True:
                    total = total + '5'
                questions.update({str(d['id']): total})
            print(questions)
            # Перебрать все вопросы (questions) и сравнить с тем что ответил пользователь (answers)
            all_questions = len(question)    # Всего вопросов
            print(all_questions)
            answered = {key: int(questions[key])-int(answers[key]) for key in questions if key in answers}
            print(answered)
            total_answered = len(answered)      # Всего отвечено
            print(total_answered)
            answered_correctly = 0              # Правильно отвечено
            for key, values in answered.items():
                if values == 0:
                    answered_correctly += 1                
            print(answered_correctly)
            print(answered_correctly/all_questions)            
            if (answered_correctly/all_questions)*100 >= limit:
                res = _('Test task completed')
            else:
                res = _('Test task failed')
            # Записать результат и перейти на страницу с протоколом выполнения
            protocol = Protocol()
            protocol.teststask_id = id
            protocol.result = (answered_correctly/all_questions)*100
            protocol.details = _('Total Questions')+ ': ' + str(all_questions) + '. ' + _('Total replied') + ': ' + str(total_answered) + '. ' + _('Correctly answered') + ': ' + str(answered_correctly) + ', (' + str((answered_correctly/all_questions)*100) + ' %). ' + res
            protocol.user_id = request.user.id
            protocol.save()
            return HttpResponseRedirect(reverse('protocol_list'))
        else:
            return render(request, "teststask/run.html", {"question": question, 'minutes': minutes, 'teststask_title': teststask_title})
    except Teststask.DoesNotExist:
        return HttpResponseNotFound("<h2>Teststask not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Протокол тестирования для менеджера (все записи)
@login_required
@group_required("Managers")
def protocol_index(request):
    protocol = Protocol.objects.all().order_by('-datep')
    return render(request, "protocol/index.html", {"protocol": protocol, })

# Протокол тестирования и решения задач для пользователя (только свои записи)
@login_required
def protocol_list(request):
    protocol = Protocol.objects.filter(user_id=request.user.id).order_by('-datep')
    decision = Decision.objects.filter(user_id=request.user.id).order_by('-dated')
    return render(request, "protocol/list.html", {"protocol": protocol,"decision": decision, })

# Список для изменения с кнопками создать, изменить, удалить
@login_required
@group_required("Managers")
def question_index(request, id):
    question = Question.objects.filter(teststask_id=id)
    teststask = Teststask.objects.get(id=id)
    return render(request, "question/index.html", {"question": question, "teststask": teststask})

# В функции create() получаем данные из запроса типа POST, сохраняем данные с помощью метода save()
# и выполняем переадресацию на корень веб-сайта (то есть на функцию index).
@login_required
@group_required("Managers")
def question_create(request, teststask_id):
    try:
        teststask = Teststask.objects.get(id=teststask_id)
        if request.method == "POST":
            question = Question()
            #question.teststask = Teststask.objects.filter(id=request.POST.get("teststask")).first()
            question.teststask_id = teststask_id       
            question.question = request.POST.get("question")
            if 'photo' in request.FILES:                
                question.photo = request.FILES['photo']    
            question.reply1 = request.POST.get("reply1")
            if (request.POST.get("ok1") == 'on'):
                question.ok1 = True
            else:
                question.ok1 = False
            question.reply2 = request.POST.get("reply2")
            if (request.POST.get("ok2") == 'on'):
                question.ok2 = True
            else:
                question.ok2 = False
            question.reply3 = request.POST.get("reply3")
            if (request.POST.get("ok3") == 'on'):
                question.ok3 = True
            else:
                question.ok3 = False
            question.reply4 = request.POST.get("reply4")
            if (request.POST.get("ok4") == 'on'):
                question.ok4 = True
            else:
                question.ok4 = False
            question.reply5 = request.POST.get("reply5")
            if (request.POST.get("ok5") == 'on'):
                question.ok5 = True
            else:
                question.ok5 = False
            question.save()
            return HttpResponseRedirect(reverse('question_index', args=(question.teststask_id,)))
        else:        
            questionform = QuestionForm(request.FILES)
            return render(request, "question/create.html", {"form": questionform, 'teststask_id': teststask_id, 'teststask': teststask,})
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
# И вначале по этому идентификатору мы пытаемся найти объект с помощью метода Question.objects.get(id=id).
# Поскольку в случае отсутствия объекта мы можем столкнуться с исключением Question.DoesNotExist,
# то соответственно нам надо обработать подобное исключение, если вдруг будет передан несуществующий идентификатор.
# И если объект не будет найден, то пользователю возващается ошибка 404 через вызов return HttpResponseNotFound().
# Если объект найден, то обработка делится на две ветви.
# Если запрос POST, то есть если пользователь отправил новые изменненые данные для объекта, то сохраняем эти данные в бд и выполняем переадресацию на корень веб-сайта.
# Если запрос GET, то отображаем пользователю страницу edit.html с формой для редактирования объекта.
@login_required
@group_required("Managers")
def question_edit(request, id):
    try:
        question = Question.objects.get(id=id)
        teststask = Teststask.objects.get(id=question.teststask_id)        
        if request.method == "POST":
            question.question = request.POST.get("question")
            if 'photo' in request.FILES:                
                question.photo = request.FILES['photo']    
            question.reply1 = request.POST.get("reply1")
            if (request.POST.get("ok1") == 'on'):
                question.ok1 = True
            else:
                question.ok1 = False
            question.reply2 = request.POST.get("reply2")
            if (request.POST.get("ok2") == 'on'):
                question.ok2 = True
            else:
                question.ok2 = False
            question.reply3 = request.POST.get("reply3")
            if (request.POST.get("ok3") == 'on'):
                question.ok3 = True
            else:
                question.ok3 = False
            question.reply4 = request.POST.get("reply4")
            if (request.POST.get("ok4") == 'on'):
                question.ok4 = True
            else:
                question.ok4 = False
            question.reply5 = request.POST.get("reply5")
            if (request.POST.get("ok5") == 'on'):
                question.ok5 = True
            else:
                question.ok5 = False        
            question.save()
            return HttpResponseRedirect(reverse('question_index', args=(question.teststask_id,))) 
        else:
            # Загрузка начальных данных
            questionform = QuestionForm(initial={'teststask': question.teststask, 'question': question.question, 'photo': question.photo,
                                                 'reply1': question.reply1,'ok1': question.ok1,'titreply2le': question.reply2,
                                                 'ok2': question.ok2,'reply3': question.reply3,'ok3': question.ok3,
                                                 'reply4': question.reply4,'ok4': question.ok4,'reply5': question.reply5,
                                                 'ok5': question.ok5,})
            return render(request, "question/edit.html", {"form": questionform, 'teststask_id': question.teststask_id, 'teststask': teststask})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Удаление данных из бд
# Функция delete аналогичным функции edit образом находит объет и выполняет его удаление.
@login_required
@group_required("Managers")
def question_delete(request, id):
    try:
        question = Question.objects.get(id=id)
        question.delete()
        return HttpResponseRedirect(reverse('question_index', args=(question.teststask_id,)))
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
@group_required("Managers")
def question_read(request, id):
    try:
        question = Question.objects.get(id=id) 
        return render(request, "question/read.html", {"question": question, "teststask_id": question.teststask_id})
    except Question.DoesNotExist:
        return HttpResponseNotFound("<h2>Question not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Задачи
@login_required
def tasks(request):
    try:
        if request.method == "POST":
            decision = Decision()
            if request.POST.get('decision1') is not None:
                decision.title = 'Задача №1'
                decision.solution = request.POST.get('decision1')
            if request.POST.get('decision2') is not None:
                decision.title = 'Задача №2'
                decision.solution = request.POST.get('decision2')
            if request.POST.get('decision3') is not None:
                decision.title = 'Задача №3'
                decision.solution = request.POST.get('decision3')
            if request.POST.get('decision4') is not None:
                decision.title = 'Задача №4'
                decision.solution = request.POST.get('decision4')
            if request.POST.get('decision5') is not None:
                decision.title = 'Задача №5'
                decision.solution = request.POST.get('decision5')
            if request.POST.get('decision6') is not None:
                decision.title = 'Задача №6'
                decision.solution = request.POST.get('decision6')
            if request.POST.get('decision7') is not None:
                decision.title = 'Задача №7'
                decision.solution = request.POST.get('decision7')
            if request.POST.get('decision8') is not None:
                decision.title = 'Задача №8'
                decision.solution = request.POST.get('decision8')
            if request.POST.get('decision9') is not None:
                decision.title = 'Задача №9'
                decision.solution = request.POST.get('decision9')
            if request.POST.get('decision10') is not None:
                decision.title = 'Задача №10'
                decision.solution = request.POST.get('decision10')        
            decision.user_id = request.user.id
            decision.save()
            #return render(request, "tasks.html")
            return HttpResponseRedirect(reverse('protocol_list'))
        else:        
            return render(request, "tasks.html")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Протокол для менеджера (все записи)
@login_required
@group_required("Managers")
def decision_index(request):
    decision = Decision.objects.all().order_by('-dated')
    return render(request, "decision/index.html", {"decision": decision, })

# Функция edit выполняет редактирование объекта.
# Функция в качестве параметра принимает идентификатор объекта в базе данных.
@login_required
@group_required("Managers")
def decision_edit(request, id):
    try:
        decision = Decision.objects.get(id=id)
        if request.method == "POST":
            decision.rating = request.POST.get("rating")                
            decision.save()
            return HttpResponseRedirect(reverse('decision_index')) 
        else:
            # Загрузка начальных данных
            decisionform = DecisionForm(initial={'dated': decision.dated, 'title': decision.title, 'solution': decision.solution,
                                                 'user': decision.user,'rating': decision.rating,})
            return render(request, "decision/edit.html", {"form": decisionform, })
    except Decision.DoesNotExist:
        return HttpResponseNotFound("<h2>Decision not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Просмотр страницы read.html для просмотра объекта.
@login_required
@group_required("Managers")
def decision_read(request, id):
    try:
        decision = Decision.objects.get(id=id) 
        return render(request, "decision/read.html", {"decision": decision,})
    except Decision.DoesNotExist:
        return HttpResponseNotFound("<h2>Decision not found</h2>")
    except Exception as exception:
        print(exception)
        return HttpResponse(exception)

# Регистрационная форма 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponseRedirect(reverse('index'))
            #return render(request, 'registration/register_done.html', {'new_user': user})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Изменение данных пользователя
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'registration/my_account.html'
    success_url = reverse_lazy('index')
    #success_url = reverse_lazy('my_account')
    def get_object(self):
        return self.request.user


