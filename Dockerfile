# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /new_lessons27-3eee

#ENV PATH /root/.local/bin:$PATH

# Копируем зависимости в контейнер
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "app.py"]