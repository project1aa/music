from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.conf import settings
import requests
from braces import views
from .forms import ContactUsForm


# control concat us page and form
class ContactUsView(views.FormValidMessageMixin, generic.CreateView):
	template_name = 'contact_us/contact_us.html'
	form_class = ContactUsForm
	form_valid_message = 'پیام شما با موفقیت ارسال شد'
	success_url = reverse_lazy('contact_us:contact_us')

	def form_valid(self, form):
		recaptcha_response = self.request.POST.get('g-recaptcha-response')
		data = {
			'secret': settings.RECAPTCHA_SERVER_KEY,
			'response': recaptcha_response
		}

        # without ssl certificat check
		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data, verify=False)

        # with ssl certificat check
        # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

		result = r.json()
		if result['success']:
			form.save()
		else:
			return super().form_invalid(form)
		return super().form_valid(form)
		#return redirect(self.success_url)
