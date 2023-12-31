# Generated by Django 4.2.2 on 2023-07-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_expensecategory_expense"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("piePerPackage", models.IntegerField()),
                ("weight", models.FloatField()),
                ("pacLong", models.FloatField()),
                ("pacWidth", models.FloatField()),
                ("pacHeight", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Volume",
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
                ("volume", models.FloatField(blank=True, null=True)),
                ("weight", models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name="expense",
            name="total",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
