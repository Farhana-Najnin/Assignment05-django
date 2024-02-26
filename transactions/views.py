from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import DepositeForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


@method_decorator(login_required, name='dispatch')
class DepositeFormView(FormView):
    template_name = 'deposite.html'
    form_class = DepositeForm

    def get(self,request,*args, **kwargs):
        deposite_form = self.form_class()
        return render(request, self.template_name, {'form':deposite_form})
    
    def post(self,request,*args, **kwargs):
        deposite_form = self.form_class(request.POST)
        if deposite_form.is_valid():
            amount = deposite_form.cleaned_data.get('amount')
            account = self.request.user.account
            account.balance += amount
            account.save(update_fields=['balance'])

            messages.success(
                request,
                f'{"{:,.2f}".format(float(amount))}$ is deposited to your account successfully!!!'
            )


            send_transaction_email(self.request.user, amount, "Deposite Message", 'deposite_email.html')
        
            return redirect('home_page')
        return render(request, self.template_name, {'form':deposite_form})
    