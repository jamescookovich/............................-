import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gosuslugi.settings')

import django

django.setup()

from go.models import Pass


def pass_loader():
    fopen = open('CodesForBot.txt')
    for i in fopen:
        new_pass = Pass()
        new_pass.password = i.strip()
        new_pass.save()


if __name__ == "__main__":
    pass_loader()
