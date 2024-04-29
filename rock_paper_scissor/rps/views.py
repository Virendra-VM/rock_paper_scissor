from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,"home.html")


def playgame(request):
    user_wins = 0
    computer_wins = 0
    draws = 0
    if request.method == 'POST':
        user_choice = request.POST.get('user_choice')
        computer_choice = random.choice(['Stone', 'Paper', 'Scissor'])  # Randomly select computer's choice
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1
        elif result == "It's a draw!":
            draws += 1
        
        # Pass user's and computer's choices to the template
        return render(request, 'playgame.html', {'user_choice': user_choice, 'computer_choice': computer_choice, 'result': result, 'user_wins': user_wins, 'computer_wins': computer_wins, 'draws': draws})

    return render(request, 'playgame.html')

def determine_winner(user_choice, computer_choice):
    # Implement your game logic to determine the winner
    if computer_choice == 'Stone' and user_choice == 'Scissor':
        return "You win!"
    elif computer_choice == 'Stone' and user_choice == 'Paper':
        return "Computer wins!"
    elif computer_choice == 'Stone' and user_choice == 'Stone':
        return "It's a draw!"
    elif computer_choice == 'Paper' and user_choice == 'Stone':
        return "Computer wins!"
    elif computer_choice == 'Paper' and user_choice == 'Scissor':
        return "You win!"
    elif computer_choice == 'Paper' and user_choice == 'Paper':
        return "It's a draw!"
    elif computer_choice == 'Scissor' and user_choice == 'Paper':
        return "Computer wins!"
    elif computer_choice == 'Scissor' and user_choice == 'Stone':
        return "You win!"
    elif computer_choice == 'Scissor' and user_choice == 'Scissor':
        return "It's a draw!"