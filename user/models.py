from django.db import models
from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings


# Create your models here.

class MyRegister(DynaModel):
    class Table:
        resource_kwargs = {
            'endpoint_url': 'settings.DB_ENDPOINT'
        }
        name = settings.DB_TABLE
        hash_key = 'created_on'
        read = 25
        write = 5

    class Schema:
        firstname = fields.String()
        lastname = fields.String()
        phonenumber = fields.String()
        address1 = fields.String()
        address2 = fields.String()
        city = fields.String()
        zipcode = fields.String()
        file = fields.String()
        created_on = fields.DateTime()




