from django.shortcuts import render, redirect
import forms
from django.contrib import messages
from django.contrib.auth.models import User
from home.models import Agendamento

def agendamento(request):
    form = forms.Agendamento()
    if str(request.method) == "POST":
        if form.is_valid():
            data = form.cleaned_data.get("nome")
            hora = form.cleaned_data.get("email")
            medicos = form.cleaned_data.get("medicos")

            dados = Agendamento.objects.order_by('-id').filter(
                data__icontains=data | hora | medicos
            )


            if not data or not hora or not medicos:
                messages.add_message(request, messages.WARNING, 'Todos os campos são obrigatórios')
                return render(request, 'agendamento.html', {'form': form})

            cons = Agendamento.objects.create(
                data=data,
                horario=hora,
                medicos=medicos,
            )
            messages.add_message(request, messages.SUCCESS, 'Agendado com sucesso')
            cons.save()
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.WARNING, 'Erro ao Agendar', {'form': form})
    else:
        return render(request, 'agendamento.html', {'form': form})

