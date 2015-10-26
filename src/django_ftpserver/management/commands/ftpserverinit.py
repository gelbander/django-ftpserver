import os, sys
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

class Command(BaseCommand):
    help = "Create root folder"

    def handle(self, *args, **options):
        try:
            ftp_root = os.path.join(settings.BASE_DIR, settings.FTPSERVER_ROOT)
        except Exception as e:
            print(e)
        if os.path.exists(ftp_root):
            sys.stdout.write(
                "Error: {ftp_root} already exists.\n".format(ftp_root=ftp_root))
        else:
            os.makedirs(ftp_root)
