from django.core.management.base import BaseCommand,CommandError
from psycopg2 import OperationalError as PsyCopgError
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """ Django command to wai database """
    help = "Wait for DB"
    def handle(self,*args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up == False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (PsyCopgError,OperationalError):
                self.stdout.write("Database unavailable waiting 1 second...")
                time.sleep(1)
