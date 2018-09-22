from django import forms
from django.conf import settings

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, HTML, Fieldset

from .models import ContactUs


class ContactUsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
		    Fieldset(
				'',
        		'name',
				'email',
				'text',
			),
            # HTML('<div class="form-group"><div class="g-recaptcha" data-sitekey="' + settings.RECAPTCHA_CLIENT_KEY + '"></div></div>'),
            HTML('<div class="g-recaptcha" data-sitekey="' + settings.RECAPTCHA_CLIENT_KEY + '"></div>'),

			ButtonHolder(
				Submit('submit', 'ارسال', css_class='btn-primary')
			)
		)

		self.fields['text'].widget.attrs = {'rows': 3}


	class Meta:
		model = ContactUs
		fields = ('name', 'email', 'text')


# class CommentForm(forms.ModelForm):
#     name = forms.CharField(label='Name', error_messages={'required': 'Please, input your name'})
#     message = forms.CharField(label='Message', widget=forms.Textarea, error_messages={'required': 'Please, input your message'})
#
#     class Meta:
#         model = Message
#
#     def __init__(self, *args, **kwargs):
#         super(CommentForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_id = 'comment_form'
#         self.helper.form_class = 'form'
#         self.helper.form_method = 'post'
#         self.helper.form_action = 'comment:index'
#         self.helper.layout = Layout(
#             Fieldset(
#                 '',
#                 'name',
#                 'message'
#             ),
#             HTML('<div class="form-group"><div class="g-recaptcha" data-sitekey="' + settings.RECAPTCHA_CLIENT_KEY + '"></div></div>'),
#             ButtonHolder(
#                 Submit('submit', 'Send')
#             )
#         )
#         self.fields['message'].widget.attrs = {'rows': 3}
