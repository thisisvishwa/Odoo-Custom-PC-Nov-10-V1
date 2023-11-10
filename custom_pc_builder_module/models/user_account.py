```python
from odoo import models, fields

class UserAccount(models.Model):
    _name = 'custom_pc_builder.user_account'
    _description = 'User Account'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Password', required=True)
    saved_builds = fields.One2many('custom_pc_builder.component', 'user_id', string='Saved Builds')
    preferences = fields.Text(string='Preferences')

    def update_user_account(self, vals):
        self.write(vals)
        return True
```