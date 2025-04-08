from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.conf import settings

# MongoDB collections
users_collection = settings.MONGO_DB['users']
teams_collection = settings.MONGO_DB['teams']
activities_collection = settings.MONGO_DB['activities']
leaderboard_collection = settings.MONGO_DB['leaderboard']
workouts_collection = settings.MONGO_DB['workouts']

# Update the base URL for the API endpoints
BASE_URL = "https://laughing-space-happiness-x7x449vq9qw2xv6-8000.app.github.dev/"

@api_view(['GET'])
def api_root(request, format=None):
    return JsonResponse({
        'users': BASE_URL + 'api/users/',
        'teams': BASE_URL + 'api/teams/',
        'activities': BASE_URL + 'api/activities/',
        'leaderboard': BASE_URL + 'api/leaderboard/',
        'workouts': BASE_URL + 'api/workouts/'
    })

# Example view for fetching users
def get_users(request):
    users = list(users_collection.find({}, {'_id': 0}))  # Exclude MongoDB's _id field
    return JsonResponse(users, safe=False)

# Example view for fetching teams
def get_teams(request):
    teams = list(teams_collection.find({}, {'_id': 0}))
    return JsonResponse(teams, safe=False)
