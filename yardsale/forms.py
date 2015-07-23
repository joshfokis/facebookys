from django import forms

from .models import Followers, Warning

class AddWarningForm(forms.ModelForm):
    class Meta:
        model = Warning
        fields = (
                  'WarningType',
                  'descript',
                  'image',
                  'image2',
                  'image3',
                  'image4',
                  'image5',
                  )
        


class FollowingForm(forms.ModelForm):

    class Meta:
        model = Followers
        fields = ('following',)
        fields
        
class NewFollowerForm(forms.ModelForm):
    
    class Meta:
        model = Followers
        fields = ('follower', 'following')