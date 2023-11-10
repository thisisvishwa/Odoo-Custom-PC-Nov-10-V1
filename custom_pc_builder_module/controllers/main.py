```python
from odoo import http
from odoo.http import request

class CustomPCBuilder(http.Controller):

    @http.route('/pc_builder/select_component', type='json', auth='user')
    def select_component(self, **kw):
        return request.env['custom_pc_builder_module.component'].select_component(kw)

    @http.route('/pc_builder/check_compatibility', type='json', auth='user')
    def check_compatibility(self, **kw):
        return request.env['custom_pc_builder_module.compatibility'].check_compatibility(kw)

    @http.route('/pc_builder/estimate_price', type='json', auth='user')
    def estimate_price(self, **kw):
        return request.env['custom_pc_builder_module.price'].estimate_price(kw)

    @http.route('/pc_builder/visualize_3d', type='json', auth='user')
    def visualize_3d(self, **kw):
        return request.env['custom_pc_builder_module.3d_visualization'].visualize_3d(kw)

    @http.route('/pc_builder/update_user_account', type='json', auth='user')
    def update_user_account(self, **kw):
        return request.env['custom_pc_builder_module.user_account'].update_user_account(kw)

    @http.route('/pc_builder/process_order', type='json', auth='user')
    def process_order(self, **kw):
        return request.env['custom_pc_builder_module.order'].process_order(kw)

    @http.route('/pc_builder/customize_build', type='json', auth='user')
    def customize_build(self, **kw):
        return request.env['custom_pc_builder_module.customization'].customize_build(kw)

    @http.route('/pc_builder/post_review', type='json', auth='user')
    def post_review(self, **kw):
        return request.env['custom_pc_builder_module.review'].post_review(kw)

    @http.route('/pc_builder/change_language', type='json', auth='user')
    def change_language(self, **kw):
        return request.env['custom_pc_builder_module.multi_language_support'].change_language(kw)

    @http.route('/pc_builder/optimize_for_mobile', type='json', auth='user')
    def optimize_for_mobile(self, **kw):
        return request.env['custom_pc_builder_module.mobile_responsiveness'].optimize_for_mobile(kw)
```