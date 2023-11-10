```javascript
var selectedComponents = [];

function checkCompatibility() {
    var compatible = true;
    var compatibilityMessage = "";

    // Check compatibility based on simple rules
    // For example, if the selected CPU and motherboard have different sockets, they are not compatible
    if (selectedComponents.cpu.socket != selectedComponents.motherboard.socket) {
        compatible = false;
        compatibilityMessage += "The selected CPU and motherboard have different sockets.\n";
    }

    // If the total power consumption of the components is more than the PSU can provide, they are not compatible
    var totalPower = selectedComponents.cpu.power + selectedComponents.gpu.power + selectedComponents.ram.power;
    if (totalPower > selectedComponents.psu.power) {
        compatible = false;
        compatibilityMessage += "The total power consumption of the components is more than the PSU can provide.\n";
    }

    // If the selected components are not compatible, display a message to the user
    if (!compatible) {
        document.getElementById('compatibility-checker').innerHTML = compatibilityMessage;
    }

    // Emit an event to notify other parts of the system that the compatibility check has been completed
    var event = new CustomEvent('compatibilityChecked', { detail: compatible });
    document.dispatchEvent(event);
}

// Listen for the 'componentSelected' event and run the compatibility check when it is received
document.addEventListener('componentSelected', function(e) {
    selectedComponents = e.detail;
    checkCompatibility();
});
```