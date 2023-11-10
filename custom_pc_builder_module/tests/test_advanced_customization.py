```python
from odoo.tests import common
from ..models import customization

class TestAdvancedCustomization(common.TransactionCase):

    def setUp(self):
        super(TestAdvancedCustomization, self).setUp()
        self.Customization = self.env['custom.pc.builder.module.customization']

    def test_customize_build(self):
        # Create a new customization
        new_customization = self.Customization.create({
            'cooling_solution': 'Liquid Cooling',
            'lighting': 'RGB',
            'casing_modification': 'Tempered Glass Side Panel'
        })

        # Check if the customization is correctly created
        self.assertEqual(new_customization.cooling_solution, 'Liquid Cooling')
        self.assertEqual(new_customization.lighting, 'RGB')
        self.assertEqual(new_customization.casing_modification, 'Tempered Glass Side Panel')

    def test_update_customization(self):
        # Create a new customization
        new_customization = self.Customization.create({
            'cooling_solution': 'Liquid Cooling',
            'lighting': 'RGB',
            'casing_modification': 'Tempered Glass Side Panel'
        })

        # Update the customization
        new_customization.write({
            'cooling_solution': 'Air Cooling',
            'lighting': 'Non-RGB',
            'casing_modification': 'Solid Side Panel'
        })

        # Check if the customization is correctly updated
        self.assertEqual(new_customization.cooling_solution, 'Air Cooling')
        self.assertEqual(new_customization.lighting, 'Non-RGB')
        self.assertEqual(new_customization.casing_modification, 'Solid Side Panel')
```