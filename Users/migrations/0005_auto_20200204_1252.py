from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20200204_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='RoomType',
            field=models.CharField(max_length=111),
        ),
    ]
