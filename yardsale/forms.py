from django import forms
from .models import Followers, Warning


class WarningForm(forms.ModelForm):
    WT1 = 'Bumping'
    WT2 = 'Pet'
    WT3 = 'Business'
    WT4 = 'Outside Links'
    WT5 = 'Price Undefined'
    WT6 = 'Other'
    warnings = (
        (WT1, 'Bumping'),
        (WT2, 'Pet'),
        (WT3, 'Business'),
        (WT4, 'Outside Links'),
        (WT5, 'Price Undefined'),
        (WT6, 'Other'),
    )
    WarningType = forms.ChoiceField(choices=warnings)
    descript = forms.Textarea()
    image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(WarningForm, self).__init__(*args, **kwargs)
        self.fields['WarningType'].label = "Select a warning type"
        
        self.fields['descript'].label = "Please provide a description"
        self.fields['image'].label = "Select an image to upload."
        self.fields['image2'].label = ""
        self.fields['image3'].label = ""
        self.fields['image4'].label = ""
        self.fields['image5'].label = ""
        
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
        
class FollowerForm(forms.ModelForm):
    
    class Meta:
        model = Followers
        fields = ('follower', 'following')