from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
import json

# Generate a random number for the game
random_number = random.randint(0, 99)

@csrf_exempt
def guess_number(request):
    global random_number
    if request.method == 'POST':
        data = json.loads(request.body)
        guessed_number = data.get('number')

        # Check if the guess is too high, too low, or correct
        if guessed_number < random_number:
            message = 'Too low!'
        elif guessed_number > random_number:
            message = 'Too high!'
        else:
            message = 'You guessed it!'
            random_number = random.randint(0, 99)  # Reset the number for a new game

        return JsonResponse({'message': message, 'number': random_number})
    return JsonResponse({'message': 'Invalid request method'}, status=400)
from django.shortcuts import render

def homepage(request):
    return render(request, 'guesser/index.html')
