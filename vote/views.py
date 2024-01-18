from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories, Candidate, Voting
from .vote import Vote


def category_details(request, slug):
    categories = get_object_or_404(Categories, slug=slug)
    candidates = categories.candidate.all()

    return render(request, 'pages/categories.html', {
        'categories' : categories,
        'candidates' : candidates
    })

#Show the candidates or voting components
def voters(request, modal_slug):
    candidate = Candidate.objects.all() [0:1]

    return render (request, '', {
        'candidate' : candidate,
    })

def createvote(request, vote_id):
    action = request.GET.get('action', '')

    if action:
        vote = 1

        vote_action = Vote(request)
        vote_action.add(vote_id, vote, True)

        return redirect('dashboard')

def vote(request, vote_id):
    vote_action = Vote(request)
    vote_action.add(vote_id)

    return redirect('dashboard')