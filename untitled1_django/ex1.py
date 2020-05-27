# это все лишнее, это временный костыль который при продакшене у тебя не сработает. Продумай логику и почитай офф документацию
import django
import os



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
django.setup()


if __name__ == "__main__":




