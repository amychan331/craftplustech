from django.utils.deprecation import MiddlewareMixin

from .apps import PortfolioConfig

class CurrentViewApplicationName(MiddlewareMixin):

  def process_view(self, request, view_func, view_args, view_kwargs):
    request.current_app = PortfolioConfig.name
