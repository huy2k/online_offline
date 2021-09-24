
from django_collect_offline.site_offline_models import site_offline_models
from django_collect_offline.offline_model import OfflineModel

offline_models = [
    'app1.CrfModel',
]

site_offline_models.register(offline_models, OfflineModel)




# list all models in app 'bcpp_household' set for offline-use
models = site_offline_models.site_models('bcpp_household', sync=True)

# list all models in app 'bcpp_household' NOT set for offline-use
# models = site_offline_models.site_models('bcpp_household', offline=False)

# # list all models in app 'bcpp_household' not set for offline-use, excluding the "historical" models
# offline_models = [m.model._meta.label_lower for m in models if 'historical' not in m.model_name]