from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.home, name='home'),

    # publish pages
    url(r'^about/author-guidelines/$', views.author_guidelines,
        name='author_guidelines'),

    # about pages
    url(r'^about/physionet/$', views.about_physionet, name='about_physionet'),
    url(r'^about/faq/$', views.faq, name='faq'),
    url(r'^about/licenses/$', views.licenses, name='licenses'),
    url(r'^about/licenses/(?P<license_slug>[\w-]+)/$', views.full_license,
        name='full_license'),

    # contact pages
    url(r'^about/contact/$', views.contact, name='contact'),

    # content pages
    url(r'^data/$', views.data, name='data'),
    url(r'^software/$', views.software, name='software'),
    url(r'^challenge/$', views.challenge, name='challenge'),

    # user account pages
    url(r'^', include('user.urls')),

    # project pages
    url(r'^projects/', include('project.urls')),
]

