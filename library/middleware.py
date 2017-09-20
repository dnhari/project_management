from django.shortcuts import render,redirect
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
class Logincall(MiddlewareMixin):
	def process_request(self,request):
		if request.path=='/login/' or request.path=='/' or request.user.is_authenticated():
			return
		else:
			return redirect('/')
