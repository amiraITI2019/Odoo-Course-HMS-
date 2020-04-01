from odoo import models,fields
class HmsDoctor(models.Model):
    _name="hms.doctors"
    _rec_name="first_name"
    first_name=fields.Char(required=True)
    last_name=fields.Char(required=True)
    image=fields.Binary("image",help="Select image here")
    department=fields.Many2one("hms.department")


