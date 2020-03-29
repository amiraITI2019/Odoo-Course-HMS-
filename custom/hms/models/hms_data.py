from odoo import models,fields
class HmsPatient(models.Model):
    _name="hms.patient"
    _rec_name="first_name"
    first_name=fields.Char()
    last_name=fields.Char()
    birth_date=fields.Date()
    history =fields.Html()
    CR_Ratio=fields.Float()
    blood_type=fields.Selection([("A","a"),("B","b"),("AB","ab"),("O","o")],default="A")
    PCR=fields.Boolean("PCR")
    image=fields.Binary("image",help="Select image here")
    address=fields.Text()
    age=fields.Integer()

