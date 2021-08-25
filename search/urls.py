from django.conf.urls import url, include
from rest_framework_extensions.routers import ExtendedDefaultRouter

from search.views import CarDocumentView

router = ExtendedDefaultRouter()

cars = router.register(r'car',
                        CarDocumentView,
                        base_name='cardocument')


urlpatterns = [
    url(r'^', include(router.urls)),
]