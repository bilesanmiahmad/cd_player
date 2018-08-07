import datetime
from django.core.management.base import BaseCommand
from pastebin.models import Paste


class Command(BaseCommand):
    help = """
    deletes pastes not updated in the last 24 hours. 
    
    Use this command in a cron job to delete older pastes"""

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(1)
        old_pastes = Paste.objects.filter(updated_on__lte=yesterday)
        old_pastes.delete()
