from django.views.generic import DetailView
from .models import Post

class blogDetail(DetailView):
    model = Post
    template_name='blog/blog_detail.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        context['post'] = post
        return context
