from django.test import TestCase

from django.utils.translation import gettext_lazy as _

import datetime
from django.utils import timezone

# Create your tests here.
# Подключение моделей
from ..models import Category, Teststask, Question, Protocol, Decision
from django.contrib.auth.models import User


# Тестирует значение параметра для всех объектов модели
def run_field_parameter_test(
        model, self_,
        field_and_parameter_value: dict,
        parameter_name: str) -> None:
    # Вначале мы получаем все объекты модели и проходимся по ним.
    # Дальше обходим словарь с полями и ожидаемыми значениями параметров.
    # После получаем реальные значения параметров, обращаясь к объекту.
    # А затем сравниваем их с ожидаемыми.
    for instance in model.objects.all():
        # Пример 1: field = "email"; expected_value = 256.
        # Пример 2: field = "email"; expected_value = "Электронная почта".
        for field, expected_value in field_and_parameter_value.items():
            parameter_real_value = getattr(
                instance._meta.get_field(field), parameter_name
            )
            self_.assertEqual(parameter_real_value, expected_value)

# Миксин для проверки verbose_name
# Мы создаём нужный метод и в нём вызываем нашу общую функцию с соответствующими параметрами.
# self.field_and_verbose_name и self.field_and_max_length берутся из класса, который наследуется от миксина.
# А именно – из метода setUpTestData класса OrganizationTests.
class TestVerboseNameMixin:
    # Метод, тестирующий verbose_name
    def run_verbose_name_test(self, model):
        run_field_parameter_test(
            model, self, self.field_and_verbose_name, 'verbose_name'
        )

# Миксин для проверки max_length
class TestMaxLengthMixin:
    def run_max_length_test(self, model):
        # Метод, тестирующий max_length
        run_field_parameter_test(
            model, self, self.field_and_max_length, 'max_length'
        )

########### Проверка моделей ###########
        
# Наследуем класс CategoryModelTest от наших миксинов.
class CategoryModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        category = Category.objects.create(title='Категория')
        category.save()
        cls.field_and_verbose_name = {
            'title': _('category_title'),                                   
        }
        cls.field_and_max_length = {
            'title': 128,
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Category)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Category)
        
# Наследуем класс TeststaskModelTest от наших миксинов.
class TeststaskModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        category = Category.objects.create(title='Категория')
        category.save()
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        teststask.save()
        cls.field_and_verbose_name = {
            'title': _('teststask_title'),                                   
            'details': _('teststask_details'),                                   
            'minutes': _('minutes'),                                   
            'limit': _('limit'),                                   
        }
        cls.field_and_max_length = {
            'title': 255,
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Teststask)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Teststask)

# Наследуем класс QuestionModelTest от наших миксинов.
class QuestionModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        category = Category.objects.create(title='Категория')
        category.save()
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        teststask.save()
        question = Question.objects.create(teststask=teststask, question='Вопрос', reply1='Ответ 1', ok1=True, reply2='Ответ 2', ok2=False, reply3='Ответ 3', ok3=False, reply4='Ответ 4', ok4=False, reply5='Ответ 5', ok5=False)
        question.save()
        cls.field_and_verbose_name = {
            'question': _('question'),                                   
            'photo': _('photo'),                                   
            'reply1': _('reply1'),                                   
            'ok1': _('ok1'),                                   
            'reply2': _('reply2'),                                   
            'ok2': _('ok2'),                                   
            'reply3': _('reply3'),                                   
            'ok3': _('ok3'),                                   
            'reply4': _('reply4'),                                   
            'ok4': _('ok4'),                                   
            'reply5': _('reply5'),                                   
            'ok5': _('ok5'),                                   
        }
        cls.field_and_max_length = {            
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Question)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Question)

# Наследуем класс ProtocolModelTest от наших миксинов.
class ProtocolModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        category = Category.objects.create(title='Категория')
        category.save()
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        teststask.save()
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()
        protocol = Protocol.objects.create(teststask=teststask, datep=timezone.now(), result=75.0, details='Тестовое задание выполненно!', user=test_user1)
        protocol.save()
        cls.field_and_verbose_name = {
            'datep': _('datep'),                                   
            'result': _('result'),                                   
            'details': _('details'),                                   
        }
        cls.field_and_max_length = {            
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Protocol)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Protocol)

# Наследуем класс DecisionModelTest от наших миксинов.
class DecisionModelTest(TestCase, TestVerboseNameMixin, TestMaxLengthMixin):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        test_user1.save()        
        decision = Decision.objects.create(dated=timezone.now(), user=test_user1, title='Задача 1', solution='Решение задачи', rating='Отлично')
        decision.save()
        cls.field_and_verbose_name = {
            'dated': _('dated'),                                   
            'title': _('task_title'),                                   
            'solution': _('solution'),                                   
            'rating': _('rating'),                                   
        }
        cls.field_and_max_length = {
            'title': 255,
        }
    # Тест параметра verbose_name
    def test_verbose_name(self):        
        super().run_verbose_name_test(Decision)
    # Тест параметра max_length
    def test_max_length(self):        
        super().run_max_length_test(Decision)