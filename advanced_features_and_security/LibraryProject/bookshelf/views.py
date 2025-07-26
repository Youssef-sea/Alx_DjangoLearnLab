# advanced_features_and_security/blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, book_list, books,
from django.urls import reverse_lazy
from .models import Article
from .forms import ExampleForm # We'll create this form next

# Function-based views with decorators
@permission_required('blog.can_view_article', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

@permission_required('blog.can_view_article', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

@permission_required('blog.can_create_article', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ExampleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'form_type': 'Create'})

@permission_required('blog.can_edit_article', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ExampleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'form_type': 'Edit'})

@permission_required('blog.can_delete_article', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/article_confirm_delete.html', {'article': article})

# Class-based views using PermissionRequiredMixin (alternative)
# class ArticleListView(PermissionRequiredMixin, ListView):
#     permission_required = 'blog.can_view_article'
#     model = Article
#     template_name = 'blog/article_list.html'
#     context_object_name = 'articles'

# class ArticleDetailView(PermissionRequiredMixin, DetailView):
#     permission_required = 'blog.can_view_article'
#     model = Article
#     template_name = 'blog/article_detail.html'
#     context_object_name = 'article'

# class ArticleCreateView(PermissionRequiredMixin, CreateView):
#     permission_required = 'blog.can_create_article'
#     model = Article
#     form_class = ExampleForm
#     template_name = 'blog/article_form.html'
#     success_url = reverse_lazy('article_list') # Redirect to list after creation

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
#     permission_required = 'blog.can_edit_article'
#     model = Article
#     form_class = ExampleForm
#     template_name = 'blog/article_form.html'
#     success_url = reverse_lazy('article_list')

# class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
#     permission_required = 'blog.can_delete_article'
#     model = Article
#     template_name = 'blog/article_confirm_delete.html'
#     success_url = reverse_lazy('article_list')