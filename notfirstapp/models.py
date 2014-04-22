from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
	firstname = models.CharField(max_length=50,blank=1,null=1)
	lastname = models.CharField(max_length=50,blank=1,null=1)
	username = models.CharField(max_length=50)
	def __unicode__(self):
		return self.username
	def isGameDeveloper(self):
		return len(Own.objects.filter(Account_id=self))>0
	isGameDeveloper.boolean=1
	isGameDeveloper.short_description='Game Developer?'

class Game(models.Model):
	gamename=models.CharField(max_length=100,default="Game")
	createTime=models.DateTimeField(auto_now_add=1)
	fk_image=models.ForeignKey('Image',null=True)
	"""docstring for Game"""
	def __unicode__(self):
		return self.gamename
	
class Figure(models.Model):
	name=models.CharField(max_length=50,default="Player")
	tag=models.CharField(max_length=50,default="Player#0000")
	User_id=models.ForeignKey(User)
	def __unicode__(self):
		return self.name+"\t tag: "+self.tag
				

class Play(models.Model):
	"""docstring for Play"""
	# User_id=models.ForeignKey(User)
	Game_id=models.ForeignKey(Game)
	Figure_id=models.ForeignKey(Figure)
	def __unicode__(self):
		return "Playing "+self.Game_id.gamename+" as "+self.Figure_id.name

class Own(models.Model):
	Game_id=models.ForeignKey(Game)
	User_id=models.ForeignKey(User)
	"""docstring for GameOwner"""
	def __unicode__(self):
		# username = Account.objects.filter(id=self.Account_id)[0].username
		# gamename = Game.objects.filter(id=self.Account_id)[0].username
		return self.User_id.username+" owns "+self.Game_id.gamename
		
class ScoreRank(models.Model):
	Figure_id=models.ForeignKey(Figure)
	Game_id=models.ForeignKey(Game)
	score=models.IntegerField(default=0)
	rank=models.IntegerField(default=0)
	achieveTime=models.DateTimeField(auto_now_add=1)
	"""docstring for Rank"""
	def __unicode__(self):
		return self.Figure_id.name+" got "+ str(self.score)+" at "+str(self.achieveTime)+" and ranks at "+str(self.rank if self.rank!=0 else 'N/A')

class TimeRank(models.Model):
	Figure_id=models.ForeignKey(Figure)
	Game_id=models.ForeignKey(Game)
	finishTime=models.TimeField(auto_now_add=0)
	rank=models.IntegerField(default=0)
	achieveTime=models.DateTimeField(auto_now_add=1)
	"""docstring for TimeRank"""
	def __unicode__(self):
		return self.Figure_id.name+" finished game in "+ str(self.finishTime)+" at "+str(self.achieveTime)+" and ranks at "+str(self.rank if self.rank!=0 else 'N/A')

class Image(models.Model):
    imagefile = models.ImageField(upload_to='Images/%Y/%m/%d')	

    def __unicode__(self):
		return self.imagefile.url
		
	