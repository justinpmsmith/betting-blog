from django.shortcuts import render
from .models import affiliate
from .models import articles
from .models import promotions
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect


def home(request):
    ad_list = affiliate.objects.all()
    promotion = promotions.objects.all()
    return render(request, 'home.html', {"ad_list": ad_list,
                                         "promotion": promotion, })


def make_money_with_sports_betting(request):
    title = "Best way to consistently make money Online with sports betting"
    promotion = promotions.objects.all()
    ad_list = affiliate.objects.all()
    article_list = articles.objects.exclude(name=title)

    return render(request, 'make_money_betting.html', {"title": title,
                                                       "ad_list": ad_list,
                                                       "article_list": article_list,
                                                       "promotion": promotion,})

def over_under(request):
    title = "The Complete Guide to Overs/Unders 2.5 Betting Strategy"
    promotion = promotions.objects.all()
    ad_list = affiliate.objects.all()
    article_list = articles.objects.exclude(name=title)

    return render(request, 'over_under.html', {"title": title,
                                                       "ad_list": ad_list,
                                                       "article_list": article_list,
                                                       "promotion": promotion,})


def landing_page(request):
    if request.method == "POST":
        email_address = request.POST['email_address']
        message = 'Here is the download link to betting to win: \n\nhttps://www.pdfdrive.com/betting-to-win-a-professional-guide-to-profitable-betting-e158751335.html.\n\nWe are here to assist you in your sports betting adventure. Feel free to contact us with any questions!!\n\n Good luck!'

        send_mail(
            'Your copy of Betting to win!', #Subject
            message,
            'wisebet.help@gmail.com',
            [email_address])
        response = redirect('/')
        return response

    return render(request, 'landing_page.html', {})
