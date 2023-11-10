```python
import unittest
from custom_pc_builder_module.models.component import Component
from custom_pc_builder_module.static.src.js.3d_visualization import visualize3D

class Test3DVisualization(unittest.TestCase):
    def setUp(self):
        self.component1 = Component('CPU', 'Intel i7', 300)
        self.component2 = Component('GPU', 'Nvidia RTX 3080', 700)
        self.selectedComponents = [self.component1, self.component2]

    def test_visualize3D(self):
        result = visualize3D(self.selectedComponents)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```