from django.test import TestCase
from .models import Profissional

class ProfissionalTestCase(TestCase):
    def setUp(self):
        Profissional.objects.create(nome_completo="Dr. Maria Silva", profissao="Médica", endereco="Rua A", contato="123456789")

    def test_nome_completo_profissional(self):
        profissional = Profissional.objects.get(nome_completo="Dr. Maria Silva")
        self.assertEqual(profissional.nome_completo, "Dr. Maria Silva")
