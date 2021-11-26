from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=20, default=None)
    crm = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=60, default=None)
    foto = models.ImageField(blank=True, upload_to='foto_produto/%y/%m/%d/')
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False, default=None)
    TIME_CHOICE = (
    ('A', '9:00'),
    ('B', '10:00'),
    ('C', '11:00'),
    ('D', '12:00'),
    ('E', '13:00'),
    ('F', '14:00'),
    ('G', '15:00'),
    )
    horario = models.CharField(max_length=1, choices=TIME_CHOICE)
    medicos = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.data, self.horario, self.medicos.nome



