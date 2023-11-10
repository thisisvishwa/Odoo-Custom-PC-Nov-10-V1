# Developer Guide

## Project Overview

This guide provides an overview of the Custom PC Builder Module for Odoo V16 & V17 Community Editions. The module allows users to select components, visualize their build, and place orders directly through the Odoo platform.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the root directory of the module.
3. Install the required dependencies using the command `pip install -r requirements.txt`.
4. Install the module in your Odoo instance.

## Code Structure

The codebase is structured into models, controllers, static resources, views, tests, and documentation.

### Models

Models define the data structure of the module. Each model corresponds to a specific feature of the module. The models are located in the `models` directory.

### Controllers

Controllers handle the business logic of the module. The main controller is located in the `controllers` directory.

### Static Resources

Static resources include JavaScript and CSS files that handle the front-end functionality and styling of the module. These files are located in the `static/src/js` and `static/src/css` directories respectively.

### Views

Views define the user interface of the module. They are written in XML and are located in the `views` directory.

### Tests

Tests ensure the functionality of the module. They are located in the `tests` directory.

### Documentation

Documentation provides detailed explanations of the module and its usage. It is located in the `docs` directory.

## Shared Dependencies

Shared dependencies include exported variables, data schemas, DOM element IDs, message names, and function names. These dependencies are used across multiple files to ensure consistency.

## Key Functions

Key functions include `selectComponent()`, `checkCompatibility()`, `estimatePrice()`, `visualize3D()`, `updateUserAccount()`, `processOrder()`, `customizeBuild()`, `postReview()`, `changeLanguage()`, and `optimizeForMobile()`. These functions handle the main functionality of the module.

## Integration Points

The module integrates with existing Odoo modules such as Inventory and Sales. It also securely handles user data.

## Troubleshooting

Refer to the `troubleshooting_guide.md` for common issues and their resolutions.

## Feedback

We welcome feedback and suggestions for improvements. Please submit your feedback through the appropriate channels.