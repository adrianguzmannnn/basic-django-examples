"""A script to insert dummy data into the Patient table."""
import uuid
from django.core.management import BaseCommand
from ContentService.models import Patient

MOCK_DATA = [
    {
        "volume_filename": "volume-2019-07-04.vol",
        "gender": "M",
        "age": 25,
        "case_history": "Pain in the abdomen",
    },
    {
        "volume_filename": "volume-2013-06-30.vol",
        "gender": "F",
        "age": 68,
        "case_history": "Strong headache",
    },
    {
        "volume_filename": "volume-2015-10-31.vol",
        "gender": "F",
        "age": 32,
        "case_history": "Swollen wrist",
    },
    {
        "volume_filename": "volume-1976-01-16.vol",
        "gender": "M",
        "age": 19,
        "case_history": "Difficulty breathing",
    },
    {
        "volume_filename": "volume-2016-01-20.vol",
        "gender": "M",
        "age": 23,
        "case_history": "Blurry eyesight",
    },
]

class Command(BaseCommand):
    """A command to insert data to the Patient model."""
    help = "Loads default data into the Patient model."

    def handle(self, *args, **options):
        if Patient.objects.exists():
            print("The table is already populated.")
            return
        print("Creating patient data.")
        for data in MOCK_DATA:
            patient = Patient()
            patient.case_uuid = data.get("case_uuid", uuid.uuid4())
            patient.volume_filename = data.get("volume_filename")
            patient.gender = data.get("gender", "M")
            patient.age = data.get("age", 30)
            patient.case_history = data.get("case_history", "Stomach cancer")
            patient.save()
        print("The insertions are completed.")
