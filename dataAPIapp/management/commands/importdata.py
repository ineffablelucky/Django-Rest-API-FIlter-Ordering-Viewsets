from django.core.management.base import BaseCommand, CommandError
from dataAPIapp.models import *
import json

class Command(BaseCommand):
    help = 'Imports Users from JSON source'

    def add_arguments(self, parser):
        parser.add_argument('--path')

    def handle(self, *args, **options):
        if options['path']:
            with open(options['path']) as json_file:
                users = json.load(json_file)
            # loads it into a list of dictionaries
                for user in users:
              # access the items as you would any dictionary
                    try:
                        new_user = UserProfile()
                        new_user.id = user["id"]
                        new_user.first_name = user["first_name"]
                        new_user.last_name = user["last_name"]
                        new_user.company_name = user["company_name"]
                        new_user.city = user["city"]
                        new_user.state = user["state"]
                        new_user.zip = user["zip"]
                        new_user.email = user["email"]
                        new_user.web = user["web"]
                        new_user.age = user["age"]
                        new_user.save()
                        print(f"New User Added: {new_user.first_name}")
                    except UserProfile.FieldError():
                        print("error..")
