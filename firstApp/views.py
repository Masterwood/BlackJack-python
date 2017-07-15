from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf

# Create your views here.
def hello(request):
    return HttpResponse('こんにちは')

def card(request):
    return render(request, 'card.html')

def welcome(request):
    name = '木村'
    dictionary = {'name' : name}
    return render(request, 'name.html', dictionary)

def cards(request):
    rank_str = []
    rank = list(range(1,14))
    for x in rank:
        rank_str.append(str(x).zfill(2))

    return render(request, 'cards.html', {'card_rank' : rank_str})

def random_cards(request):
    import random
    suits = ['S', 'H', 'D', 'C']
    ranks = range(1,14)
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)

    card1 = deck.pop()
    card2 = deck.pop()

    dictionary = {
        'suit' : card1[1],
        'rank' : str(card1[0]).zfill(2),
        'suit2' : card2[1],
        'rank2' : str(card2[0]).zfill(2),
    }
    return render(request, 'display_cards.html', dictionary)


# welcome2

def form_test(request):
    if request.method == 'POST':
        print(request.POST)
        return welcome2(request, request.POST['name'])

    elif request.method == 'GET':
        dictionary = {}
        dictionary.update(csrf(request))
        return render(request, 'form.html', dictionary)

def welcome2(request, name):
    # name = '木村'
    dictionary = {'name' : name}
    return render(request, 'name.html', dictionary)

# form_card

def form_card(request):
    if request.method == 'GET':
        rank_list = []
        for i in range(1,14):
            rank_list.append(str(i))
        dictionary = {'rank_list':rank_list}

        dictionary.update(csrf(request))
        return render(request, 'select_card.html', dictionary)

    if request.method == 'POST':
        suit = request.POST['suit']
        rank = request.POST['rank'].zfill(2)
        dictionary = {'suit':suit, 'rank':rank}
        print(suit,rank)
        return render(request,'display_card2.html', dictionary)
