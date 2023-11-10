```javascript
let selectedComponents = [];
let totalPrice = 0;

// Function to estimate the price of selected components
function estimatePrice() {
    totalPrice = 0;
    selectedComponents.forEach(component => {
        totalPrice += component.price;
    });
    updatePriceDisplay();
}

// Function to update the price display
function updatePriceDisplay() {
    let priceDisplay = document.getElementById('price-estimator');
    priceDisplay.textContent = `Total Price: $${totalPrice.toFixed(2)}`;
}

// Event listener for component selection
document.addEventListener('componentSelected', (event) => {
    selectedComponents.push(event.detail);
    estimatePrice();
});

// Event listener for component deselection
document.addEventListener('componentDeselected', (event) => {
    let index = selectedComponents.findIndex(component => component.id === event.detail.id);
    if (index !== -1) {
        selectedComponents.splice(index, 1);
        estimatePrice();
    }
});
```