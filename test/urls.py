from django.conf.urls import url, patterns
from django.conf.urls.static import static
from task.views import SignUp, ListView, IndexView
from test.settings import STATIC_ROOT, STATIC_URL

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name="index_view"),
                       url(r'^add/', SignUp.as_view(), name="signup_view"),
                       url(r'^list/', ListView.as_view(), name="list_view"),
                       )

urlpatterns += patterns('',
                        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                            {'document_root': STATIC_ROOT}),
                        )

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

