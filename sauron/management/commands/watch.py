from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Spin up sauron to watch.'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Sauron is watching!')
        )
        subprocess.run('python manage.py runserver', shell=True)
