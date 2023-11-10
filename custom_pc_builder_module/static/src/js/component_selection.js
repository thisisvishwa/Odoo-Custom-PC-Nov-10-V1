```javascript
var selectedComponents = [];

// Function to select a component
function selectComponent(component) {
    // Check if the component is already selected
    if (!selectedComponents.includes(component)) {
        // Add the component to the selected components array
        selectedComponents.push(component);
        
        // Emit the componentSelected event
        var event = new CustomEvent('componentSelected', { detail: component });
        document.getElementById('component-selection').dispatchEvent(event);
    }
}

// Event listener for the component selection interface
document.getElementById('component-selection').addEventListener('click', function(event) {
    var component = event.target.dataset.component;
    selectComponent(component);
});
```