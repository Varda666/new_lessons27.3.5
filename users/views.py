from django.urls import reverse_lazy
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from lms_service.tasks import check_last_visit
from users.models import User, UserSubscriptionUpdates
from lms_service.permissions import IsOwnerOrNot, IsOwner
from users.serializers import UserSerializer, UserSubscriptionUpdatesSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            # Сохранение объекта перед тем, как установить ему пароль
            self.object.set_password(self.object.password)
            self.object.save()

        return super().form_valid(form)


class UserSubscriptionUpdatesCreateView(CreateAPIView):
    queryset = UserSubscriptionUpdates.objects.all()
    serializer_class = UserSubscriptionUpdatesSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        if check_last_visit(pk=self.request.user):
            pass
        self.request.user.is_active = False

class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all(), UserSubscriptionUpdates.objects.all()
    serializer_class = UserSerializer, UserSubscriptionUpdatesSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrNot]

class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsOwner]


class UserSubscriptionUpdatesDestroyView(DestroyAPIView):
    queryset = UserSubscriptionUpdates.objects.all()
    serializer_class = UserSubscriptionUpdatesSerializer
    permission_classes = [IsAdminUser | IsOwner]


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
