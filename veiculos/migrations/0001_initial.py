# Generated by Django 5.2.3 on 2025-06-30 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Veiculo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "placa",
                    models.CharField(max_length=7, unique=True, verbose_name="Placa"),
                ),
                ("modelo", models.CharField(max_length=100, verbose_name="Modelo")),
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("CARRO", "Carro"),
                            ("MOTO", "Moto"),
                            ("CAMINHAO", "Caminhão"),
                        ],
                        max_length=10,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("DISPONIVEL", "Disponível"),
                            ("INDISPONIVEL", "Indisponível"),
                        ],
                        default="DISPONIVEL",
                        max_length=12,
                        verbose_name="Status",
                    ),
                ),
                (
                    "data_cadastro",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de cadastro"
                    ),
                ),
            ],
            options={
                "verbose_name": "Veículo",
                "verbose_name_plural": "Veículos",
                "ordering": ["placa"],
            },
        ),
    ]
