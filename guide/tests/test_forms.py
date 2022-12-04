from django.test import TestCase

# Create your tests here.

from django.utils.translation import gettext_lazy as _
from ..models import Category, Teststask, Question, Protocol, Decision
from ..forms import CategoryForm, TeststaskForm, QuestionForm, DecisionForm
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
        
# Тесты формы CategoryFormTests
class CategoryFormTests(TestCase):
    # Тест лейблов полей        
    def test_field_labels(self):
        form = CategoryForm()
        title_label = form.fields['title'].label
        self.assertEqual(title_label, _('category_title'))        
    # Тест создания новой записи
    def test_form_save(self):
        data = {"title": "Категория"}        
        form = CategoryForm(data=data)
        self.assertTrue(form.is_valid())        
        self.assertIsInstance(form.save(), Category)
        print("CategoryFormTests.test_form_save OK")     
              
# Тесты формы TeststaskFormTests
class TeststaskFormTests(TestCase):
    # Тест лейблов полей        
    def test_field_labels(self):
        form = TeststaskForm()
        category_label = form.fields['category'].label
        self.assertEqual(category_label, _('category'))
        title_label = form.fields['title'].label
        self.assertEqual(title_label, _('teststask_title'))
        details_label = form.fields['details'].label
        self.assertEqual(details_label, _('teststask_details'))
        minutes_label = form.fields['minutes'].label
        self.assertEqual(minutes_label, _('minutes'))
        limit_label = form.fields['limit'].label
        self.assertEqual(limit_label, _('limit'))        
        print("TeststaskFormTests.test_field_labels OK")
    # Тест создания новой записи
    def test_form_save(self):
        category = Category.objects.create(title='Категория')
        data = {"category": category, 
                "title": "Название теста", 
                "details": "Тест по космонавтике",
                "minutes": 10,
                "limit": 10}        
        form = TeststaskForm(data=data)
        self.assertTrue(form.is_valid())        
        self.assertIsInstance(form.save(), Teststask)
        print("TeststaskFormTests.test_form_save OK")

# Тесты формы QuestionFormTests
class QuestionFormTests(TestCase):
    # Тест лейблов полей        
    def test_field_labels(self):
        form = QuestionForm()
        question_label = form.fields['question'].label
        self.assertEqual(question_label, _('question'))
        photo_label = form.fields['photo'].label
        self.assertEqual(photo_label, _('photo'))
        reply1_label = form.fields['reply1'].label
        self.assertEqual(reply1_label, _('reply1'))
        ok1_label = form.fields['ok1'].label
        self.assertEqual(ok1_label, _('ok1'))
        reply2_label = form.fields['reply2'].label
        self.assertEqual(reply2_label, _('reply2'))
        ok2_label = form.fields['ok2'].label
        self.assertEqual(ok2_label, _('ok2'))
        reply3_label = form.fields['reply3'].label
        self.assertEqual(reply3_label, _('reply3'))
        ok3_label = form.fields['ok3'].label
        self.assertEqual(ok3_label, _('ok3'))
        reply4_label = form.fields['reply4'].label
        self.assertEqual(reply4_label, _('reply4'))
        ok4_label = form.fields['ok4'].label
        self.assertEqual(ok4_label, _('ok4'))
        reply5_label = form.fields['reply5'].label
        self.assertEqual(reply5_label, _('reply5'))
        ok5_label = form.fields['ok5'].label
        self.assertEqual(ok5_label, _('ok5'))
        print("QuestionFormTests.test_field_labels OK")
    # Тест создания новой записи
    def test_form_save(self):
        category = Category.objects.create(title='Категория')
        teststask = Teststask.objects.create(category=category, title='Название теста', details='Тест по космонавтике', minutes=10, limit=80)
        data = {"question": "Вопрос", 
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
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())        
        #self.assertIsInstance(form.save(), Question)
        print("QuestionFormTests.test_form_save OK")

# Тесты формы QuestionFormTests
class DecisionFormTests(TestCase):
    # Тест лейблов полей        
    def test_field_labels(self):
        form = DecisionForm()
        title_label = form.fields['title'].label
        self.assertEqual(title_label, _('task_title'))
        solution_label = form.fields['solution'].label
        self.assertEqual(solution_label, _('solution'))
        rating_label = form.fields['rating'].label
        self.assertEqual(rating_label, _('rating'))        
        print("QuestionFormTests.test_field_labels OK")
    # Тест создания новой записи
    def test_form_save(self):
        test_user1 = User.objects.create_user(username='testuser1', password='Tt12345+')
        data = {"user": test_user1, 
                "title": "Задача 1", 
                "solution": "Решение задачи",
                "rating": "Отлично"}        
        form = QuestionForm(data=data)
        self.assertTrue(form.is_valid())        
        self.assertIsInstance(form.save(), Question)
        print("QuestionFormTests.test_form_save OK")