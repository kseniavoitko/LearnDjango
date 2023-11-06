from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from django.views import View
from mongoengine.errors import NotUniqueError

from utils.models import Authors, Qoutes

from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    quotes = Qoutes.objects()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author(request, author: str):
    try:
        author = Authors.objects.get(fullname=author)
    except:
        author = None
    context = {"author": author}
    return render(request, "quotes/author.html", context)


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            fullname = form.cleaned_data["fullname"]
            messages.success(request, f"Author '{fullname}' was created...")
            return render(
                request, "quotes/create_author.html", context={"form": AuthorForm()}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, "quotes/create_author.html", context={"form": form})

    context = {"form": AuthorForm()}
    return render(request, "quotes/create_author.html", context)


@login_required
def create_quote(request, id: int = 0):
    authors = Authors.objects.all()

    if request.method == "POST":
        form = QuoteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.quote = form.cleaned_data["quote"]
            new_quote.author = Authors.objects.filter(
                pk=form.cleaned_data["author"]
            ).get()
            new_quote.save()
            print(1)
            messages.success(request, "Quote was added....")

        else:
            messages.error(request, "Not added....")
            return render(
                request, "quotes/create_quote.html", {"authors": authors, "form": form}
            )

    return render(
        request, "quotes/create_quote.html", {"authors": authors, "form": QuoteForm()}
    )


class CreateAuthorView(LoginRequiredMixin, View):
    form_class = AuthorForm
    template_name = "quotes/create_author.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            author = Authors(**form.cleaned_data)
            try:
                author.save()
            except NotUniqueError:
                messages.error(request, f"Author '{author.fullname}' already present in DB")
            else:
                messages.success(request, f"Author '{author.fullname}' was created...")
            return render(
                request, self.template_name, context={"form": self.form_class}
            )
        else:
            messages.error(request, "Not added...")
            return render(request, self.template_name, context={"form": form})
