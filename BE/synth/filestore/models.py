from django.db import models
import uuid
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns


#model to store invoices
class Invoice(DjangoCassandraModel) :
    invoice_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    stored_time = columns.DateTime()
    invoice_source = columns.Text()
    internal_invoice = columns.Text()