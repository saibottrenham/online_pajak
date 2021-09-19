from django.db import models

class TaxDataModel(models.Model):
    user_id = models.CharField(max_length=200, null=True)
    company_id = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    npwp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    post_code = models.IntegerField(null=True)
    invoice_id = models.CharField(max_length=200, null=True)
    vendor_id = models.CharField(max_length=200,null=True)
    vendor_name = models.CharField(max_length=200, null=True)
    commercial_invoice_number = models.CharField(max_length=200, null=True)
    transaction_type = models.CharField(max_length=200, null=True)
    status_start = models.CharField(max_length=200, null=True)
    status_tax_summary = models.CharField(max_length=200, null=True)
    invoice_date = models.DateTimeField(null=True)
    due_date = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    unitprice = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    gross_amount = models.IntegerField(null=True)
    tax_amount = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    tax_period = models.CharField(max_length=200, null=True)
    revision = models.IntegerField(null=True)
    reported_date = models.DateTimeField(null=True)
    reported_status = models.CharField(max_length=200, null=True)
    reported_status_desc = models.CharField(max_length=200, null=True)
    tax_type = models.CharField(max_length=200, null=True)
    tax_document_number = models.CharField(max_length=200, null=True)
    tax_document_date = models.DateTimeField(null=True)
    approved_date = models.DateTimeField(null=True)
