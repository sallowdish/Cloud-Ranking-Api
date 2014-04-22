from django import forms
from .models import *
from django.contrib.auth.models import User

class AccountForm(forms.ModelForm):
    password= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    # newUser=None

    class Meta:
        model=Account


    def is_valid(self):
        # import pdb; pdb.set_trace();
        emptyError='This field is required'
        isFilledUp=True
        flag=super(AccountForm,self).is_valid()
        #check all field is filled up
        if not bool(self.data['username']):
            self.errors['username']=emptyError
        if not bool(self.data['password']):
            self.errors['password']=emptyError
        # if not bool(self.data['email']):
        #     self.errors['email']=emptyError
        if len(self.errors)==0:
            #check if username is valid
            existList=[user.username for user in User.objects.all()]
            if self.data['username'] in existList:
                self.errors['Invaild Username']='Username has been used by someone else!'
                isFilledUp=False
        else:#fail to find all required info
            isFilledUp=False
        # import pdb; pdb.set_trace()
        return flag and isFilledUp

    def save(self):
        user=User.objects.create_user(
            username=self.data['username'],
            password=self.data['password'],
            email=self.data['email'],
            first_name=self.data['firstname'],
            last_name=self.data['lastname']
        )
        self.newUser=user

class GameForm(forms.ModelForm):
    class Meta:
    	model= Game
        field=['gamename','fk_image']

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass

class ImageForm(forms.Form):
    imagefile = forms.ImageField(
        label='Select a image',
        help_text='max. 42 megabytes'
    )

class FigureForm(forms.ModelForm):
    class Meta:
        model=Figure
        field=['name']

class PlayForm(forms.ModelForm):
    class Meta:
        model=Play

class ScoreRankForm(forms.ModelForm):
    # username=models.CharField(max_length=50)
    # playername=models.CharField(max_length=50)
    # gamename=models.CharField(max_length=50)
    class Meta:
        model=ScoreRank
        exclude=['rank']