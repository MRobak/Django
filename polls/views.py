from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import loader

from .models import Song, Toplist

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_toplist_list'

    def get_queryset(self):
        """Return the last five published toplist."""
        return Toplist.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Toplist
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Toplist
    template_name = 'polls/results.html'

def vote(request, toplist_id):
    toplist = get_object_or_404(Toplist, pk=toplist_id)
    try:
        selected_song = toplist.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'toplist': toplist,
            'error_message': "You didn't select a song.",
        })
    else:
        selected_song.votes += 1
        selected_song.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(toplist.id,)))

