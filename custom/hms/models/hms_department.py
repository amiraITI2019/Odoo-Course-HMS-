from odoo import models,fields
class HmsDepartment(models.Model):
    _name="hms.department"
    name=fields.Char()
    is_opened=fields.Boolean("is opened")
    capacity=fields.Integer()
    def name_get(self):
        res = []
        for field in self:
           res.append((field.id,'name: %s : capacity: %s' %(field.name,field.capacity)))
        return res
   