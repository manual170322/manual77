from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

def new_tetstask(apps, schema_editor):
    user = User.objects.create_superuser(username='root', email='manual170322@mail.ru', password='MAhd1234+@')
    managers = Group.objects.get_or_create(name = 'Managers')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Суперпользователь создан")

    user = User.objects.create_user(username='manager', password='BsOs1234+@')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Менеджер создан")

    user = User.objects.create_user(username='user1', password='not12345+@')
    user = User.objects.create_user(username='user2', password='not12345+@')
    user = User.objects.create_user(username='user3', password='not12345+@')
    user = User.objects.create_user(username='user4', password='not12345+@')
    user = User.objects.create_user(username='user5', password='not12345+@')
    print("Пользователи созданы")

    Category = apps.get_model("guide", "Category")

    category = Category()
    category.id = 1
    category.title = 'Основы Информационной безопасности'   
    category.save()
    print("Категории созданы")

    # Тестовые задания #
    
    Teststask = apps.get_model("guide", "Teststask")

    teststask = Teststask()
    teststask.id = 1
    teststask.category_id = 1
    teststask.title = 'Тест №1'
    teststask.details = 'Информационная безопасность - тест №1'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()

    teststask = Teststask()
    teststask.id = 2
    teststask.category_id = 1
    teststask.title = 'Тест №2'
    teststask.details = 'Информационная безопасность - тест №2'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()

    teststask = Teststask()
    teststask.id = 3
    teststask.category_id = 1
    teststask.title = 'Тест №3'
    teststask.details = 'Информационная безопасность - тест №3'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()

    print("Тестовые задания созданы")

    # Вопросы к тестовым заданиям  #


    Question = apps.get_model("guide", "Question")

    question = Question()
    question.teststask_id = 1
    question.question = 'К правовым методам, обеспечивающим информационную безопасность, относятся:'
    question.reply1 = 'Разработка аппаратных средств обеспечения правовых данных'
    question.ok1 = False
    question.reply2 = 'Разработка и установка во всех компьютерных правовых сетях журналов учета действий'
    question.ok2 = False
    question.reply3 = 'Разработка и конкретизация правовых нормативных актов обеспечения безопасности'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Основными источниками угроз информационной безопасности являются все указанное в списке:'
    question.reply1 = 'Хищение жестких дисков, подключение к сети, инсайдерство'
    question.ok1 = False
    question.reply2 = 'Перехват данных, хищение данных, изменение архитектуры системы'
    question.ok2 = True
    question.reply3 = 'Хищение данных, подкуп системных администраторов, нарушение регламента работы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Виды информационной безопасности:'
    question.reply1 = 'Персональная, корпоративная, государственная'
    question.ok1 = True
    question.reply2 = 'Клиентская, серверная, сетевая'
    question.ok2 = False
    question.reply3 = 'Локальная, глобальная, смешанная'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Цели информационной безопасности – своевременное обнаружение, предупреждение:'
    question.reply1 = 'несанкционированного доступа, воздействия в сети'
    question.ok1 = True
    question.reply2 = 'инсайдерства в организации'
    question.ok2 = False
    question.reply3 = 'чрезвычайных ситуаций'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Основные объекты информационной безопасности:'
    question.reply1 = 'Компьютерные сети, базы данных'
    question.ok1 = True
    question.reply2 = 'Информационные системы, психологическое состояние пользователей'
    question.ok2 = False
    question.reply3 = 'Бизнес-ориентированные, коммерческие системы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
 
    question = Question()
    question.teststask_id = 1
    question.question = 'Основными рисками информационной безопасности являются:'
    question.reply1 = 'Искажение, уменьшение объема, перекодировка информации'
    question.ok1 = False
    question.reply2 = 'Техническое вмешательство, выведение из строя оборудования сети'
    question.ok2 = False
    question.reply3 = 'Потеря, искажение, утечка информации'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'К основным принципам обеспечения информационной безопасности относится:'
    question.reply1 = 'Экономической эффективности системы безопасности'
    question.ok1 = True
    question.reply2 = 'Многоплатформенной реализации системы'
    question.ok2 = False
    question.reply3 = 'Усиления защищенности всех звеньев системы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Основными субъектами информационной безопасности являются:'
    question.reply1 = 'руководители, менеджеры, администраторы компаний'
    question.ok1 = False
    question.reply2 = 'органы права, государства, бизнеса'
    question.ok2 = True
    question.reply3 = 'сетевые базы данных, фаерволлы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'К основным функциям системы безопасности можно отнести все перечисленное:'
    question.reply1 = 'Установление регламента, аудит системы, выявление рисков'
    question.ok1 = True
    question.reply2 = 'Установка новых офисных приложений, смена хостинг-компании'
    question.ok2 = False
    question.reply3 = 'Внедрение аутентификации, проверки контактных данных пользователей'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Принципом информационной безопасности является принцип недопущения:'
    question.reply1 = 'Неоправданных ограничений при работе в сети (системе)'
    question.ok1 = True
    question.reply2 = 'Рисков безопасности сети, системы'
    question.ok2 = False
    question.reply3 = 'Презумпции секретности'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Принципом политики информационной безопасности является принцип:'
    question.reply1 = 'Невозможности миновать защитные средства сети (системы)'
    question.ok1 = True
    question.reply2 = 'Усиления основного звена сети, системы'
    question.ok2 = False
    question.reply3 = 'Полного блокирования доступа при риск-ситуациях'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Принципом политики информационной безопасности является принцип:'
    question.reply1 = 'Усиления защищенности самого незащищенного звена сети (системы)'
    question.ok1 = True
    question.reply2 = 'Перехода в безопасное состояние работы сети, системы'
    question.ok2 = False
    question.reply3 = 'Полного доступа пользователей ко всем ресурсам сети, системы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Принципом политики информационной безопасности является принцип:'
    question.reply1 = 'Разделения доступа (обязанностей, привилегий) клиентам сети (системы)'
    question.ok1 = True
    question.reply2 = 'Одноуровневой защиты сети, системы'
    question.ok2 = False
    question.reply3 = 'Совместимых, однотипных программно-технических средств сети, системы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'К основным типам средств воздействия на компьютерную сеть относится:'
    question.reply1 = 'Компьютерный сбой'
    question.ok1 = False
    question.reply2 = 'Логические закладки («мины»)'
    question.ok2 = True
    question.reply3 = 'Аварийное отключение питания'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Когда получен спам по e-mail с приложенным файлом, следует:'
    question.reply1 = 'Прочитать приложение, если оно не содержит ничего ценного – удалить'
    question.ok1 = False
    question.reply2 = 'Сохранить приложение в парке «Спам», выяснить затем IP-адрес генератора спама'
    question.ok2 = False
    question.reply3 = 'Удалить письмо с приложением, не раскрывая (не читая) его'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Принцип Кирхгофа:'
    question.reply1 = 'Секретность ключа определена секретностью открытого сообщения'
    question.ok1 = False
    question.reply2 = 'Секретность информации определена скоростью передачи данных'
    question.ok2 = False
    question.reply3 = 'Секретность закрытого сообщения определяется секретностью ключа'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'ЭЦП – это:'
    question.reply1 = 'Электронно-цифровой преобразователь'
    question.ok1 = False
    question.reply2 = 'Электронно-цифровая подпись'
    question.ok2 = True
    question.reply3 = 'Электронно-цифровой процессор'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
   
    question = Question()
    question.teststask_id = 2
    question.question = 'Наиболее распространены угрозы информационной безопасности корпоративной системы:'
    question.reply1 = 'Покупка нелицензионного ПО'
    question.ok1 = False
    question.reply2 = 'Ошибки эксплуатации и неумышленного изменения режима работы системы'
    question.ok2 = True
    question.reply3 = 'Сознательного внедрения сетевых вирусов '
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Наиболее распространены угрозы информационной безопасности сети:'
    question.reply1 = 'Распределенный доступ клиент, отказ оборудования'
    question.ok1 = False
    question.reply2 = 'Моральный износ сети, инсайдерство'
    question.ok2 = False
    question.reply3 = 'Сбой (отказ) оборудования, нелегальное копирование данных'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Наиболее распространены средства воздействия на сеть офиса:'
    question.reply1 = 'Слабый трафик, информационный обман, вирусы в интернет'
    question.ok1 = False
    question.reply2 = 'Вирусы в сети, логические мины (закладки), информационный перехват'
    question.ok2 = True
    question.reply3 = 'Компьютерные сбои, изменение админстрирования, топологии'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Утечкой информации в системе называется ситуация, характеризуемая:'
    question.reply1 = 'Потерей данных в системе'
    question.ok1 = True
    question.reply2 = 'Изменением формы информации'
    question.ok2 = False
    question.reply3 = 'Изменением содержания информации'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Свойствами информации, наиболее актуальными при обеспечении информационной безопасности являются:'
    question.reply1 = 'Целостность'
    question.ok1 = True
    question.reply2 = 'Доступность'
    question.ok2 = False
    question.reply3 = 'Актуальность'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Угроза информационной системе (компьютерной сети) – это:'
    question.reply1 = 'Вероятное событие'
    question.ok1 = True
    question.reply2 = 'Детерминированное (всегда определенное) событие'
    question.ok2 = False
    question.reply3 = 'Событие, происходящее периодически'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Информация, которую следует защищать (по нормативам, правилам сети, системы) называется:'
    question.reply1 = 'Регламентированной'
    question.ok1 = False
    question.reply2 = 'Правовой'
    question.ok2 = False
    question.reply3 = 'Защищаемой'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Разновидностями угроз безопасности (сети, системы) являются все перчисленное в списке:'
    question.reply1 = 'Личные, корпоративные, социальные, национальные'
    question.ok1 = False
    question.reply2 = 'Программные, технические, организационные, технологические'
    question.ok2 = True
    question.reply3 = 'Серверные, клиентские, спутниковые, наземные'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Окончательно, ответственность за защищенность данных в компьютерной сети несет:'
    question.reply1 = 'Владелец сети'
    question.ok1 = True
    question.reply2 = 'Администратор сети'
    question.ok2 = False
    question.reply3 = 'Пользователь сети'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Политика безопасности в системе (сети) – это комплекс:'
    question.reply1 = 'Руководств, требований обеспечения необходимого уровня безопасности'
    question.ok1 = True
    question.reply2 = 'Инструкций, алгоритмов поведения пользователя в сети'
    question.ok2 = False
    question.reply3 = 'Нормы информационного права, соблюдаемые в сети'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Наиболее важным при реализации защитных мер политики безопасности является:'
    question.reply1 = 'Аудит, анализ затрат на проведение защитных мер'
    question.ok1 = False
    question.reply2 = 'Аудит, анализ безопасности'
    question.ok2 = False
    question.reply3 = 'Аудит, анализ уязвимостей, риск-ситуаций'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'К правовым методам, обеспечивающим информационную безопасность, относятся:'
    question.reply1 = 'Разработка аппаратных средств обеспечения правовых данных'
    question.ok1 = False
    question.reply2 = 'Разработка и установка во всех компьютерных правовых сетях журналов учета действий'
    question.ok2 = False
    question.reply3 = 'Разработка и конкретизация правовых нормативных актов обеспечения безопасности'
    question.ok3 = True
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 3
    question.question = 'Основными источниками угроз информационной безопасности являются все указанное в списке:'
    question.reply1 = 'Хищение жестких дисков, подключение к сети, инсайдерство'
    question.ok1 = False
    question.reply2 = 'Перехват данных, хищение данных, изменение архитектуры системы'
    question.ok2 = True
    question.reply3 = 'Хищение данных, подкуп системных администраторов, нарушение регламента работы'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    print("Вопросы к тестовым заданиям созданы")
    
class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_tetstask),
    ]
