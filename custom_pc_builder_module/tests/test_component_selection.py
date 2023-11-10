```python
from odoo.tests import common
from custom_pc_builder_module.models.component import Component

class TestComponentSelection(common.TransactionCase):

    def setUp(self):
        super(TestComponentSelection, self).setUp()
        self.Component = self.env['component']

    def test_01_check_component_selection(self):
        # Create a new component
        self.component = self.Component.create({
            'name': 'Test Component',
            'type': 'CPU',
            'price': 200.00,
        })

        # Check if the component is correctly created
        self.assertEqual(self.component.name, 'Test Component')
        self.assertEqual(self.component.type, 'CPU')
        self.assertEqual(self.component.price, 200.00)

    def test_02_select_component(self):
        # Select the created component
        selected_component = self.Component.select_component(self.component.id)

        # Check if the component is correctly selected
        self.assertEqual(selected_component, self.component)

    def test_03_deselect_component(self):
        # Deselect the selected component
        deselected_component = self.Component.deselect_component(self.component.id)

        # Check if the component is correctly deselected
        self.assertEqual(deselected_component, None)
```