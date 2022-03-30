from django.db.models.signals import post_save
from NormalApp.models import NormalModel

# a handler
def PostSave_NormalModel(sender, *args, **kwargs):
    print("log : a post saved in 'NormalModel'")


# add a event listener with type "post_save" and handler "PostSave_NormalModel"
# this listener when run that publisher event is the "NormalModel"
# this is a design pattern with common name "observer / listener / event"
post_save.connect(PostSave_NormalModel, sender=NormalModel)
