from django.shortcuts import render,render_to_response,get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse,QueryDict,HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import *
from django.views import generic
from django.contrib.auth.models import User
from notfirstapp.models import *
from .forms import *
# Create your views here.
class IndexView(ListView):
	# current_game=Game.objects.all()
	model=Game
	template_name='notfirstapp/index.html'
	context_object_name='game_list'

	def get_context_data(self, **kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		game_list=Game.objects.order_by('-createTime')[:4]
		context['game_list']=game_list
		context['user']=self.request.user
		return context
	# return HttpResponse(template.render(context))

class SignUpView(FormView):
    form_class=AccountForm
    template_name='notfirstapp/signup.html'


    def form_valid(self,form):
        # form_class=get_form_class
        # import pdb; pdb.set_trace()
        
        

        form.save()
        
        # import pdb; pdb.set_trace()
        # user.save()
        return self.get_success_url();


    def form_invalid(self,form):
        # formWithError = AccountForm(data=form.data)
        # import pdb; pdb.set_trace()
        return render(self.request,'notfirstapp/signup.html',{'form':form});

    def get_success_url(self):
        return HttpResponse(render(self.request,'notfirstapp/loginframe.html',{'alert':'SignUp Successd!'}))

    # def get_fail_url(self):
    #     return render(self.request,'notfirstapp/signup.html',{'form':form});

class ProfileView(TemplateView):
	"""docstring for ClassName"""
	template_name='notfirstapp/profile.html'


	def get_context_data(self,**kwargs):
		context=super(ProfileView,self).get_context_data(**kwargs)
		context['user']=self.request.user
		return context
		


class FigureFormView(CreateView):
	"""docstring for FigureFormView"""
	context_object_name='figureform.html'
	form_class=FigureForm

	def post(self, request, *args, **kwargs):
		form=self.form_class(request.POST)

                if form.is_valid():
                # newGame=Game(gamename=form.data[''])
                    return self.form_valid(form)
                else:
                    return self.form_invalid(form)

        def form_valid(self,form):
                self.object = form.save()
                # self.object=obj
                # self.object.save()
                self.id=self.object.id
                return HttpResponseRedirect(self.get_success_url())
	
    # def get_form(self, form_class):
    #     form = (super(GameCreateView, self)).get_form(form_class)
    #     current_account = Account.objects.all()
    #     form.fields['fk'].queryset = current_images 
    #     return form

        def get_success_url(self):
                return reverse('FigureDetailPage',kwargs={'pk': self.id})

class ScoreRankView(ListView):
    template_name='notfirstapp/ranklist.html'
    model=ScoreRank

    context_object_name='rank_list'

    def get_context_data(self, **kwargs):
        gameid=self.kwargs['pk']
        game=get_object_or_404(Game,pk=gameid)

        context=super(ScoreRankView,self).get_context_data(**kwargs)
        rank_list=ScoreRank.objects.filter(Game_id=gameid).order_by('-score')
        # import pdb
        # pdb.set_trace()
        context['rank_list']=rank_list
        context['game']=game
        # context['user']=self.request.user
        return context

class GameListView(ListView):
	# form_class=GameForm
	template_name = "notfirstapp/gamelist.html"
	context_object_name = 'game_list'
	queryset=Game.objects.order_by('-createTime')


class GameCreateView(CreateView):
    # Handle file upload
    template_name="notfirstapp/gameform.html"
    form_class=GameForm

    def post(self, request, *args, **kwargs):
    	# data=form.data
    	# self.object = None
     #    form = self.get_form(self.form_class)
     #    targetID=request.POST['fk_image']
     #    form.instance.fk_image=Image.objects.get(id=targetID)

        form=self.form_class(request.POST)

        if form.is_valid():
        	# newGame=Game(gamename=form.data[''])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self,form):
    	self.object = form.save()
    	# self.object=obj
    	# self.object.save()
    	self.id=self.object.id
    	return HttpResponseRedirect(self.get_success_url())

    def get_form(self, form_class):
        form = (super(GameCreateView, self)).get_form(form_class)
        current_images = Image.objects.all()
        form.fields['fk_image'].queryset = current_images 
        return form

    def get_context_data(self, **kwargs):
        context = super(GameCreateView, self).get_context_data(**kwargs)
        context['current_path'] = self.request.get_full_path()
#        import pdb;pdb.set_trace()
        return context

    def get_success_url(self):
    	return reverse('GameDetailPage',kwargs={'pk': self.id})

class GameDetailView(DetailView):
    model = Game
    template_name = 'notfirstapp/gamedetail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GameDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['appname'] = 'notfirstapp'
        context['back_url']=reverse('GameListPage')
        return context


class ImageView(FormView):
    # Handle file upload
    template_name="notfirstapp/imageform.html"
    form_class=ImageForm

    def get_context_data(self, **kwargs):
    	context = super(ImageView, self).get_context_data(**kwargs)
    	context['uploaded']=Image.objects.all();
    	return context;

    def form_valid(self,form):
    	newImage=Image(
    		imagefile=self.get_form_kwargs().get('files')['imagefile'])	
    	newImage.save();
    	self.id=newImage.id

    	return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
    	return reverse('ImageFormPage')

class ImageDetailView(DetailView):
    model = Image
    template_name = 'notfirstapp/imagedetial.html'
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['appname'] = 'notfirstapp'
        return context


class ImageListView(ListView):
    model = Image
    template_name = 'notfirstapp/imagelist.html'
    context_object_name = 'imagelist'
    queryset = Image.objects.all()
    # if request.method == 'POST':
    #     form = ImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newimage = Image(imagefile = request.FILES['imagefile'])
    #         newimage.save()

    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('notfirstapp.views.ImageListContoller'))
    # else:
    #     form = ImageForm() # A empty, unbound form

    # # Load documents for the list page
    # images = Image.objects.all()

    # # Render list page with the documents and the form
    # return render_to_response(
    #     'notfirstapp/imagelist.html',
    #     {'Images': images, 'form': form},
    #     context_instance=RequestContext(request)
    # )
