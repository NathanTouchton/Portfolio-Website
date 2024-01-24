from django.views.generic.base import TemplateView

# Create your views here.

class HomepageView(TemplateView):
    """This is the view for displaying the homepage."""
    template_name = "portfolio_main/homepage.html"
