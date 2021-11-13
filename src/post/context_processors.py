from .models import Banner

def banner_context(request):
	mybanner = Banner.objects.all()

	return dict(mybanner=mybanner)