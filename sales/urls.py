from sales.models import Quote
from django.urls import path, include
from . import views


urlpatterns = [
    path("send_email", views.email, name="email"),
    path("quote-list", views.QuoteList.as_view(), name="quotelist"),
    path("quote-detail/<int:pk>", views.QuoteDetail.as_view(), name="quote-detail"),
    path("quote-create/<int:pk>", views.create_quote, name="create-quote"),
    path("quote-item-add/<int:qid>", views.add_item, name="add-item"),
    path("quote-item-delete/<int:pk>",
         views.delete_quote_item, name="delete-item"),
    path("add-followup/<int:orgid>", views.add_follow_up, name="add-followup"),
    path("show-followup",views.show_followup, name="showfollowuo"),
]
