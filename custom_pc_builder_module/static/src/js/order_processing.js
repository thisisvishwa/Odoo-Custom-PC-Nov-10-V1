```javascript
odoo.define('custom_pc_builder_module.order_processing', function (require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var _t = core._t;
    var QWeb = core.qweb;

    var OrderProcessing = {
        processOrder: function() {
            var self = this;
            var orderData = {
                'selectedComponents': self.selectedComponents,
                'totalPrice': self.totalPrice,
                'userAccount': self.userAccount
            };

            ajax.jsonRpc('/shop/confirm_order', 'call', {
                'order_data': orderData
            }).then(function (data) {
                if (data.success) {
                    self._displaySuccessMessage(_t("Your order has been successfully processed."));
                    core.bus.trigger('orderPlaced', orderData);
                } else {
                    self._displayErrorMessage(_t("There was an error processing your order. Please try again."));
                }
            });
        },

        _displaySuccessMessage: function(message) {
            this.do_notify(_t("Success"), message);
        },

        _displayErrorMessage: function(message) {
            this.do_warn(_t("Error"), message);
        }
    };

    return OrderProcessing;
});
```