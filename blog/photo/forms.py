from django.forms import inlineformset_factory #인라인 폼셋 반환
from photo.models import Album, Photo

PhotoInlineFormSet = inlineformset_factory(Album, Photo,
       fields = ['image', 'title', 'description'],
       extra = 2)