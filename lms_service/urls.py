from django.urls import path
from rest_framework import routers
from django.contrib import admin

from lms_service.views.lesson import *
from lms_service.views.course import *
from lms_service.views.payment import PaymentListView, PaymentRetrieveView, PaymentUpdateView, PaymentCreateView, \
    PaymentDestroyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LessonListView.as_view(), name='lesson_list'),
    path('<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
    path('create/', LessonCreateView.as_view(), name='lesson_create'),
    path('delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson_delete'),
    path('payment/', PaymentListView.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentRetrieveView.as_view(), name='payment_detail'),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payment/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payment/delete/<int:pk>/', PaymentDestroyView.as_view(), name='payment_delete'),


    ]

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns += router.urls
