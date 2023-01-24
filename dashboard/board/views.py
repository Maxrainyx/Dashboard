from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from .filters import CommentFilter
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from .forms import PostForm, CommentForm


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('com_approve'))
    comment.approved = True
    comment.save()
    return HttpResponseRedirect(reverse('profile'))


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('com_delete'))
    comment.delete()
    return HttpResponseRedirect(reverse('profile'))


class PostList(ListView):
    """ View for the list of Posts  """
    model = Post
    ordering = '-created'  # The order by [created time, from newer]
    template_name = 'posts.html'
    paginate_by = 5  # Amount of the posts on the page
    context_object_name = 'posts'


class PostDetail(DetailView):
    """ Generic View for a single post with its id """
    model = Post
    template_name = 'post_detail.html'
    # The name for the Post chosen by user
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        """ Overwrite method to get comments on the page """
        context = super(PostDetail, self).get_context_data(**kwargs)
        users = []
        comments = list(
            Comment.objects.filter(post_id=self.kwargs["pk"]).values(
                'id',
                'text',
                'author__username',
                'created',
                'approved',
            )
        )
        if comments:
            context['comments'] = {
                'text': comments,
            }
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    """ Generic View to CREATE a new Post(redirected to the new page because of Post models get_absolute_url method) """
    permission_required = ('board.add_post',)  # Permissions to create the post
    form_class = PostForm
    model = Post
    template_name = 'post_add.html'

    def form_valid(self, form):
        """ The method to check if the form is valid """
        post = form.save(commit=False)
        post.author_id = self.request.user.id
        return super().form_valid(form)


class PostUpdate(PermissionRequiredMixin, UpdateView):
    """ Generic View to UPDATE the Post """
    permission_required = ('board.change_post',)  # Permissions to update the post
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    """ Generic View to DELETE the Post """
    permission_required = ('board.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class UserView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    model = Comment
    context_object_name = 'coms'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class CommentCreate(LoginRequiredMixin, CreateView):
    """ Generic View to CREATE a new Comment (redirected to the new page) """
    permission_required = ('board.add_comment',)  # Permissions to create the post
    form_class = CommentForm
    model = Comment
    template_name = 'comment_update.html'
    context_object_name = 'comment'

    def form_valid(self, form):
        """ The method to check if the form is valid """
        comment = form.save(commit=False)
        comment.author_id = self.request.user.id
        comment.post_id = self.kwargs["pk"]
        if comment.post.author_id == self.request.user.id:
            comment.approved = True
        return super().form_valid(form)

