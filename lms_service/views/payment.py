from datetime import datetime

import stripe
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from lms_service.models import Payment, Lesson, Course
from lms_service.permissions import IsModerator, IsOwner
from lms_service.serializers.payment import PaymentSerializer


class PaymentCreateView(CreateAPIView):
    # queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        paid_lesson = Lesson.objects.get(id=kwargs.get('pk'))
        paid_course = Course.objects.get(id=kwargs.get('pk'))
        stripe.api_key = 'pk_test_51OEbeRDOFdoxv7piNTKgVoRsb0C43xLwsHTZZGhEGuXNiDL85v6DPfMUaWu3XTXBAO1KonVExO6mCug8CybpvzF500ITvnSrYS'
        response = stripe.Payment.create(
            amount=2000,
            currency="rub",
            automatic_payment_methods={"enabled": True},
        )
        stripe.Payment.confirm(
            response.id,
            payment_method='tr-card_visa'
        )
        user = self.request.id
        payment_id = response.id
        data = {
            'pay_id': payment_id,
            'user': user,
            'pay_date': datetime.now(),
            'paid_course': paid_course,
            'paid_lesson': paid_lesson,
            'payment_amount': response.amount,
            'is_confirmed': True,
        }
        serializer = self.get_serializer(data)
        serializer.is_valid()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)










class PaymentUpdateView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsModerator | IsOwner]


class PaymentRetrieveView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator | IsOwner]


class PaymentDestroyView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminUser | IsOwner]


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['pay_date']
    permission_classes = [IsAuthenticatedOrReadOnly | IsModerator | IsOwner]