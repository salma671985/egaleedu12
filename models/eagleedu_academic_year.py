from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime,date
from calendar import monthrange

# class AcademyRoomNo(models.Model):
#     _name='education.rooms'
#     name=fields.Char('Room Name')
#     code=fields.Integer('Room No')
#     capacity=fields.Integer('Capacity')
#     amenities_ids = fields.One2many('education.class.amenities', 'room_id', string='Amenities')

class EagleeduAcademicYear(models.Model):
    _name = 'eagleedu.academic.year'
    _description = 'Academic Year'
    _order = 'sequence asc'
    _rec_name = 'name'
    name = fields.Char(string='Year Name', required=True, help='Name of academic year')
    academic_year_code = fields.Char(string='Code', required=True, help='Code of academic year')
    sequence = fields.Integer(string='Sequence', required=True)
    academic_year_start_date = fields.Date(string='Start date', required=True, help='Starting date of academic year')
    academic_year_end_date = fields.Date(string='End date', required=True, help='Ending of academic year')
    academic_year_description = fields.Text(string='Description', help="Description about the academic year")
    active = fields.Boolean('Active', default=True,
                            help="If unchecked, it will allow you to hide the Academic Year without removing it.")

    @api.model
    def create(self, vals):
        """Over riding the create method and assigning the
        sequence for the newly creating record"""
        vals['sequence'] = self.env['ir.sequence'].next_by_code('eagleedu.academic.year')
        res = super(EagleeduAcademicYear, self).create(vals)
        return res





