from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.test import Client

from ..models import Category, Teststask, Question, Protocol, Decision

from django.contrib.auth.models import User, Group

import datetime
from django.utils import timezone
       
class CategoryViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('category_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'category/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/category/index/')
        self.assertRedirects(response, '/login/?next=/category/index/')             
        response = self.client.post('/category/index/')
        self.assertRedirects(response, '/login/?next=/category/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        data = {
            'title': 'Категория'
        }
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('category_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/category/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Category.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('category_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)
        
class TeststaskViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('teststask_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'teststask/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/teststask/index/')
        self.assertRedirects(response, '/login/?next=/teststask/index/')             
        response = self.client.post('/teststask/index/')
        self.assertRedirects(response, '/login/?next=/teststask/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        category = Category.objects.create(title='Категория')
        category.save();
        data = {"category": category.id, 
                "title": "Название теста", 
                "details": "Тест по космонавтике",
                "minutes": 10,
                "limit": 10}    
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('teststask_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/teststask/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Teststask.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('teststask_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)

class QuestionViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('question_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'question/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/question/index/')
        self.assertRedirects(response, '/login/?next=/question/index/')             
        response = self.client.post('/question/index/')
        self.assertRedirects(response, '/login/?next=/question/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        category = Category.objects.create(title='Категория')
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        data = {"teststask": teststask,
                "question": "Вопрос", 
                "reply1": "Ответ 1", 
                "ok1": True,
                "reply2": "Ответ 2", 
                "ok2": False,
                "reply3": "Ответ 3", 
                "ok3": True,
                "reply4": "Ответ 4", 
                "ok4": False,
                "reply5": "Ответ 5", 
                "ok5": False}        
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('question_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/question/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Question.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('question_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)

class ProtocolViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('protocol_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'protocol/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/protocol/index/')
        self.assertRedirects(response, '/login/?next=/protocol/index/')             
        response = self.client.post('/protocol/index/')
        self.assertRedirects(response, '/login/?next=/protocol/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        category = Category.objects.create(title='Категория')
        category.save()
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        teststask.save()
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()

        data = {
            "teststask": teststask,
            "datep": timezone.now(),
            "result": 75.0,
            "details": "Тестовое задание выполненно!",
            "user": test_user1
        }
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('protocol_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/protocol/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Protocol.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('protocol_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)

class DecisionViewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        # Группа менеджеров уже создана при миграции
        managers = Group.objects.get(name='Managers')
        # Пользователь с ролью менеджера 
        managers.user_set.add(test_user1)
    def test_logged_in_uses_correct_template(self):
        # Вход пользователя
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Переход на указанную страницу (представление)
        resp = self.client.get(reverse('decision_index'))
        # Проверка что пользователь залогинился
        self.assertEqual(str(resp.context['user']), 'testuser1')
        # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'decision/index.html')
    # Проверка представление для неаутентифицированного пользователя,
    # если пользователь неавторизованный - перенаправит на страницу входа
    # LOGIN_REDIRECT_URL = '/', LOGIN_URL = '/login/'
    def test_view_deny_anonymous(self):
        response = self.client.get('/decision/index/')
        self.assertRedirects(response, '/login/?next=/decision/index/')             
        response = self.client.post('/decision/index/')
        self.assertRedirects(response, '/login/?next=/decision/index/')
    # Проверка POST-запроса, GET-запроса
    def test_view_post(self):
        # Добавляемые в запросе данные        
        data = {"user": test_user1, 
                "title": "Задача 1", 
                "solution": "Решение задачи",
                "rating": "Отлично"}
        # Залогиниться
        login = self.client.login(username='testuser1', password='Tt12345+')
        # Отправить POST-запрос присваивание follow=True, в запросе, гарантирует что запрос вернёт окончательный URL-адрес пункта назначения (следовательно проверяется /catalog/, а не /)
        response = self.client.post(reverse('decision_create'), data, follow=True)
        # Проверить возврат на страницу index после успешного сохранения
        self.assertRedirects(response, '/decision/index/')        
        self.assertEqual( response.status_code, 200)
        # Получить id последнего добавленного объекта
        latest_obj = Decision.objects.latest('id')
        #print("latest obj id ", latest_obj.id)
        # Получить страницу с добавленным объектом
        response = self.client.get(reverse('decision_read', kwargs={'id': latest_obj.id,}))
        self.assertEqual(response.status_code, 200)