from odoo import models,fields,api
class HmsPatient(models.Model):
    _name="hms.patients"
    _rec_name="first_name"
    first_name=fields.Char(required=True)
    last_name=fields.Char(required=True)
    birth_date=fields.Date()
    history =fields.Html()
    CR_Ratio=fields.Float()
    blood_type=fields.Selection([("A","a"),("B","b"),("AB","ab"),("O","o")],default="A")
    PCR=fields.Boolean("PCR")
    image=fields.Binary("image",help="Select image here")
    address=fields.Text()
    age=fields.Integer()
    department=fields.Many2one("hms.department")
    doctor=fields.Many2one("hms.doctors")
    log_history=fields.Many2one('patient.log')
    state=fields.Selection([("G","Good"),("U","Undetermined"),("F","Fair"), ("S","Serious")],default="U")
    changed=fields.Boolean("changed",default=False)
    email=fields.Char(unique=True)
    # @api.onchange('age')
    # def _onchange_age(self):
    #     self.vals.history.attrs.invisible=0
    @api.onchange('state')
    def _onchange_state(self):
        self.changed=True
        






