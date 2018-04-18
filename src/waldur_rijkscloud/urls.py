from . import views


def register_in(router):
    router.register(r'rijkscloud', views.ServiceViewSet, base_name='rijkscloud')
    router.register(r'rijkscloud-service-project-link', views.ServiceProjectLinkViewSet,
                    base_name='rijkscloud-spl')
    router.register(r'rijkscloud-flavors', views.FlavorViewSet, base_name='rijkscloud-flavor')
    router.register(r'rijkscloud-volumes', views.VolumeViewSet, base_name='rijkscloud-volume')
    router.register(r'rijkscloud-instances', views.InstanceViewSet, base_name='rijkscloud-instance')