from odoo import models,fields
class PatientLog(models.Model):
    _name="patient.log"
    Created_by=fields.Char(required=True)
    date=fields.Date()
    description=fields.Char(required=True)
