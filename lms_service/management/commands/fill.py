from django.core.management import BaseCommand

from lms_service.models import Payment, Lesson, Course
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        pass


        # user3, _ = User.objects.get_or_create(email='admin1@mail.ru', defaults={
        #     'first_name': 'Ivan',
        #     'last_name': 'Ivanov',
        #     'phone': '+79118245324',
        #     'country': 'RF',
        #     'is_superuser': True,
        #     'is_staff': True
        #      })

        # course_list = [
        #     {'name': 'Анг. язык для начинающих', 'description': 'Получение уровня А',
        #      'lessons_count': 2, 'user': user3},
        #     {'name': 'Нем. язык для начинающих', 'description': 'Получение уровня А',
        #      'lessons_count': 2, 'user': user3},
        # ]
        # course_for_create = []
        # for item in course_list:
        #     course_for_create.append(Course(**item))
        # Course.objects.all().delete()
        # Course.objects.bulk_create(course_for_create)



        # #
        # #
        # course1, _ = Course.objects.get_or_create(name='Анг. язык для начинающих', defaults={
        #     'description': 'Получение уровня А',
        #     'lessons_count': 2
        #  })
        # course2, _ = Course.objects.get_or_create(name='Нем. язык для начинающих', defaults={
        #     'description': 'Получение уровня А',
        #     'lessons_count': 2
        # })
        #
        # lesson_list = [
        #     {'name': 'Урок анг. яз 1', 'description': 'Знакомство с анг. языком', 'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course1, 'user': user3},
        #     {'name': 'Урок анг. яз 2', 'description': 'Изучение алфавита анг. яз', 'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course1, 'user': user3},
        #     {'name': 'Урок нем. яз 1', 'description': 'Знакомство с нем. языком', 'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course2, 'user': user3},
        #     {'name': 'Урок нем. яз 2', 'description': 'Изучение алфавита нем. яз', 'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course2, 'user': user3},
        # ]
        # lesson_for_create = []
        # for item in lesson_list:
        #     lesson_for_create.append(Lesson(**item))
        # Lesson.objects.all().delete()
        # Lesson.objects.bulk_create(lesson_for_create)
        #
        #
        #
        #
        #
        # user_list = [
        #     {'email': 'user1@mil.ru', 'first_name': 'Ivan',
        #      'last_name': 'Ivanov', 'phone': '+79118245324', 'country': 'RF',
        #      'is_superuser': True, 'is_staff': True},
        #     {'email': 'user2@mil.ru', 'first_name': 'Petr',
        #      'last_name': 'Petrov', 'phone': '+79118245423', 'country': 'RF'},
        #     {'email': 'user3@mil.ru', 'first_name': 'Olga',
        #      'last_name': 'Covrova', 'phone': '+79114285324', 'country': 'RF'},
        # ]
        # user_for_create = []
        # for item in user_list:
        #     user_for_create.append(User(**item))
        # User.objects.all().delete()
        # User.objects.bulk_create(course_for_create)
        #
        #
        #
        #
        # course1, _ = Course.objects.get_or_create(name='Анг. язык для начинающих', defaults={
        #     'description': 'Получение уровня А',
        #     'lessons_count': 2
        # })
        # course2, _ = Course.objects.get_or_create(name='Нем. язык для начинающих', defaults={
        #     'description': 'Получение уровня А',
        #     'lessons_count': 2
        # })
        #
        # lesson1, _ = Lesson.objects.get_or_create(name='Урок анг. яз 1', defaults={
        #     'description': 'Знакомство с анг. языком',
        #     'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course1
        # })
        # lesson2, _ = Lesson.objects.get_or_create(name='Урок нем. яз 2', defaults={
        #     'description': 'Изучение алфавита нем. яз',
        #     'link': 'https://ru.stackoverflow.com/questions/1388409/django', 'course': course2
        # })
        #
        # user1, _ = User.objects.get_or_create(email='user2@mil.ru', defaults={
        #     'first_name': 'Petr', 'last_name': 'Petrov', 'phone': '+79118245423', 'country': 'RF'
        # })
        # user2, _ = User.objects.get_or_create(email='user3@mil.ru', defaults={
        #     'first_name': 'Olga', 'last_name': 'Covrova', 'phone': '+79114285324', 'country': 'RF'
        # })
        #
        # payment_list = [
        #     {'user': user1, 'pay_date': '2022-11-21', 'paid_course': course1,
        #      'paid_lesson': lesson1, 'payment_amount': 3000, 'payment_method': 'transfer'},
        #     {'user': user2, 'pay_date': '2022-10-22', 'paid_course': course2,
        #      'paid_lesson': '', 'payment_amount': 2000, 'payment_method': 'cash'},
        # ]
        # payment_for_create = []
        # for item in payment_list:
        #     payment_for_create.append(Payment(**item))
        # Payment.objects.all().delete()
        # Payment.objects.bulk_create(payment_for_create)
        #
        #
