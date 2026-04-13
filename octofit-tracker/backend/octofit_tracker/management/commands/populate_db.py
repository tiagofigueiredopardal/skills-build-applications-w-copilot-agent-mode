from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models as djongo_models
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users
        users = [
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "captain@marvel.com", "team": "marvel"},
            {"name": "Natasha Romanoff", "email": "blackwidow@marvel.com", "team": "marvel"},
        ]
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {"name": "marvel", "members": ["Tony Stark", "Steve Rogers", "Natasha Romanoff"]},
            {"name": "dc", "members": ["Clark Kent", "Bruce Wayne", "Diana Prince"]},
        ]
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {"user": "Clark Kent", "activity": "Flight", "duration": 60},
            {"user": "Bruce Wayne", "activity": "Martial Arts", "duration": 45},
            {"user": "Tony Stark", "activity": "Engineering", "duration": 120},
            {"user": "Steve Rogers", "activity": "Running", "duration": 30},
        ]
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {"user": "Clark Kent", "points": 1000},
            {"user": "Tony Stark", "points": 950},
            {"user": "Bruce Wayne", "points": 900},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {"user": "Diana Prince", "workout": "Strength", "reps": 50},
            {"user": "Natasha Romanoff", "workout": "Agility", "reps": 40},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
