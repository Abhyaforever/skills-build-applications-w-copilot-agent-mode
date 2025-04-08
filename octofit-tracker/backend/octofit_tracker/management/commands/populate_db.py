from django.core.management.base import BaseCommand
from django.conf import settings
from octofit_tracker.test_data import test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        db = settings.MONGO_DB

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Populate users
        db.users.insert_many(test_data['users'])

        # Populate teams
        db.teams.insert_many(test_data['teams'])

        # Populate activities
        db.activities.insert_many(test_data['activities'])

        # Populate leaderboard
        db.leaderboard.insert_many(test_data['leaderboard'])

        # Populate workouts
        db.workouts.insert_many(test_data['workouts'])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
