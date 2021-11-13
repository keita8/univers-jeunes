from .models import Galerie

def galerie_context(request):
	magalerie = Galerie.objects.all()
	return dict(magalerie=magalerie)