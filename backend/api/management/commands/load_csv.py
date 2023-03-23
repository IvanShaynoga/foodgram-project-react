"""Импорт данных из csv файлов."""

import csv

from django.conf import settings
from django.core.management import BaseCommand
from api.models import Ingredient

TABLES = {
    Ingredient: "ingredients.csv",
}


class Command(BaseCommand):
    """Команда."""

    def handle(self, *args, **kwargs):
        """Обработчик."""
        for model, csv_f in TABLES.items():
            with open(
                f'{settings.BASE_DIR}/data/{csv_f}',
                'r',
                encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                model.objects.bulk_create(
                    model(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Все данные загружены'))
