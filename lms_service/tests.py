from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms_service.models import Course, Lesson, Payment
from users.models import User


class ModelCreateTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            user_role='moderator',
            email='test@mail.com',
            first_name='Name',
            last_name='Last',
            phone='8976',
            country='RF',
        )
        self.user.set_password('123qwe')
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            name='Анг. язык для начинающих',
            description='Получение уровня А',
            lessons_count=2,
            user=self.user,
        )

        self.lesson = Lesson.objects.create(
            name='Урок анг. яз 1',
            description='Знакомство с анг. языком',
            link='https://www.youtube.com/123',
            course=self.course,
            user=self.user,

        )



    def test_get_list(self):
        response = self.client.get(
            reverse('lms_service:lesson_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    "id": self.lesson.id,
                    "link": self.lesson.link,
                    "name": self.lesson.name,
                    "img": None,
                    "description": self.lesson.description,
                    "course": Course.objects.get(pk=self.course.pk).name,
                    "user": self.lesson.user.email,
                },
            ]
        )

    def test_lesson_create(self):
        data = {'name': 'Урок анг. яз 2',
                'description': 'Знакомство с анг. языком',
                'link': 'https://ru.stackoverflow.com/questions/1388409/django',
                'course': Course.objects.get(name='Анг. язык для начинающих').name,
                'user': User.objects.get(email='test@mail.com'),
                }
        response = self.client.post(
            reverse('lms_service:lesson_create'),
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_update(self):
        # responce = self.client.get(
        #     reverse(
        #         'lms_service:lesson_detail',
        #         kwargs={'pk': self.lesson.pk},
        #     ))
        data = {'name': 'Урок франц. яз 2',
                'description': 'Знакомство с франц. языком',
                'link': 'https://ru.stackoverflow.com/questions/1388409/django',
                'course': Course.objects.get(name='Анг. язык для начинающих').name
                }
        responce = self.client.put(
            reverse(
                'lms_service:lesson_update',
                kwargs={'pk': self.lesson.pk}),
            data=data,
            format='json')
        self.assertEquals(
            Lesson.objects.get(pk=self.lesson.pk).name,
            'Урок франц. яз 2'
        )

    def test_lesson_delete(self):
        response = self.client.delete(
            reverse('lms_service:lesson_delete', kwargs={'pk': self.lesson.pk})
        )
        self.assertEqual(response.status_code, 204)
        self.assertEquals(
            Lesson.objects.all().count(),
            0
        )