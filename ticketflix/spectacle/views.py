from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .models import Spectacle, Movie, Play, Show


class SpectacleDetailView(DetailView):
    model = Spectacle
    template_name = 'spectacle/detail.html'

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle


class SpectacleListView(ListView):
    model = Spectacle
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SpectacleCreateView(CreateView):
    model = Spectacle
    template_name = 'spectacle/form.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class SpectacleDeleteView(DeleteView):
    model = Spectacle

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list',
    )


class SpectacleUpdateView(UpdateView):
    model = Spectacle
    template_name = 'spectacle/form.html'
    fields = [
        'name',
        'spectacle_type',
        'status',
        'duration',
        'poster',
        'classification',
    ]

    def get_object(self, queryset=None):
        spectacle = Spectacle.objects.get(
            id=self.kwargs.get('id')
        )
        return spectacle

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'spectacle/movie_form.html'
    fields = [
        'synopsis',
        'diretor',
        'cast',
        'producer',
        'writer',
        'gender',
        'trailer',
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        spectacles = Spectacle.objects.all()
        objects = []
        for spectacle in spectacles:
            related = Spectacle.objects.get_related_object(spectacle)
            if related is None:
                objects.append(spectacle)

        context['spectacles'] = objects
        return context

    def form_valid(self, form):
        data = form.data
        spectacle = Spectacle.objects.get(id=int(data['spectacle']))
        data['name'] = spectacle.name
        data['status'] = spectacle.status
        data['poster'] = spectacle.poster
        data['duration'] = spectacle.duration
        data['classification'] = spectacle.classification
        data['spectacle_type'] = spectacle.spectacle_type
        data['spectacle_id'] = spectacle.id
        form.data = data
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class PlayCreateView(CreateView):
    model = Play
    template_name = 'spectacle/play_form.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )


class ShowCreateView(CreateView):
    model = Show
    template_name = 'spectacle/play_form.html'
    fields = '__all__'

    def form_valid(self, form):
        return super().form_valid(form)

    success_url = reverse_lazy(
        viewname='spectacle:spectacle-list'
    )