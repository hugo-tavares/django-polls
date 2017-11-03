"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


'''
    regex: syntax for matching patterns in strings

    view: when django finds a regex match, it calls the specified view function
    with an HttpRequest object as the first argument and any "captured" values
    from the regex as other arguments. If the regex uses simple captures,
    values are passed as positional arguments; if it uses named captures,
    values are passed as keyword arguments.

    kwargs: arbitrary keyword arguments can be passed in a dictionary to the
    target view

    name: naming your URL lets you refer to it unambiguously from elsewhere
    in django, especially from within templates. This powerful feature allows
    you to make global changes to the URL patterns of your project while only
    touching a single file.
    '''
urlpatterns = [
    # you should always use include() when you include other URL patterns
    # admin.site.urls is the only exception to this.

    # the url() function is passed 4 arguments, two required: regex and view,
    # and two optional: kwargs and name.

    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
