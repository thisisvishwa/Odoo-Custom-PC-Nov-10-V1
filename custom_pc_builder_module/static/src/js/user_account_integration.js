```javascript
odoo.define('custom_pc_builder_module.user_account_integration', function (require) {
    "use strict";

    var rpc = require('web.rpc');
    var session = require('web.session');

    var userAccount = {};

    function updateUserAccount() {
        rpc.query({
            model: 'res.users',
            method: 'read',
            args: [session.uid, ['name', 'email', 'selectedComponents', 'totalPrice']],
        }).then(function (data) {
            userAccount = {
                name: data[0].name,
                email: data[0].email,
                selectedComponents: data[0].selectedComponents,
                totalPrice: data[0].totalPrice
            };
            $(document).trigger('accountUpdated', userAccount);
        });
    }

    function saveBuild() {
        rpc.query({
            model: 'res.users',
            method: 'write',
            args: [session.uid, {
                selectedComponents: selectedComponents,
                totalPrice: totalPrice
            }],
        }).then(function () {
            updateUserAccount();
        });
    }

    $(document).on('componentSelected priceUpdated', function () {
        saveBuild();
    });

    updateUserAccount();

});
```