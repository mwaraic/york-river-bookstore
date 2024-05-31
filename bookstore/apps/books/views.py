from bookstore.apps.yrb.models import YrbOffer, YrbClub, YrbCategory
from django.shortcuts import render
from .filters import PriceFilter, FilteredListView
from django.http import Http404


def super_category_view(request):

    all_clubs = YrbClub.objects.all()
    context = {'all_clubs': all_clubs
               }
    return render(request, 'supercategory.html', context)


def category_view(request, club):
    try:
        club = YrbClub.objects.get(club=club)
    except:
        raise Http404('Page does not exist')

    context = {'all_categories': YrbCategory.objects.all(),
               'club': club
               }
    return render(request, 'category.html', context)


class BookView(FilteredListView):

    filterset_class = PriceFilter
    template_name = 'booklist.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            YrbClub.objects.get(club=self.kwargs.get('club'))
            if (self.kwargs.get('cat').lower() == 'all'):
                pass
            else:
                YrbCategory.objects.get(cat=self.kwargs.get('cat').lower())
        except:
            raise Http404('Page does not exist')

        context['all_categories'] = YrbCategory.objects.all()
        context['club'] = self.kwargs.get('club')
        context['cat'] = self.kwargs.get('cat')
        return context


def book_detail_view(request, OfferID):
    try:
        YrbOffer.objects.get(pk=OfferID)
    except:
        raise Http404('Page does not exist')
    book = YrbOffer.objects.filter(pk=OfferID).values(
        'offerid', 'title', 'price', 'club', 'year', 'title_id__cat', 'title_id__language', 'title_id__weight')
    return render(request, 'book.html', {'book': book})
