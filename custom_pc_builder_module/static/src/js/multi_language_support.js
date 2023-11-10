```javascript
// Multi-language support for Custom PC Builder Module

// List of supported languages
const supportedLanguages = ['en', 'es', 'fr', 'de', 'it', 'pt'];

// Default language
let currentLanguage = 'en';

// Language dictionary
const languageDictionary = {
    en: {
        // English translations here
    },
    es: {
        // Spanish translations here
    },
    fr: {
        // French translations here
    },
    de: {
        // German translations here
    },
    it: {
        // Italian translations here
    },
    pt: {
        // Portuguese translations here
    }
};

// Function to change language
function changeLanguage(newLanguage) {
    if (supportedLanguages.includes(newLanguage)) {
        currentLanguage = newLanguage;
        updateInterfaceLanguage();
    } else {
        console.error(`Unsupported language: ${newLanguage}`);
    }
}

// Function to update interface language
function updateInterfaceLanguage() {
    const elements = document.querySelectorAll('[data-translate]');

    elements.forEach(element => {
        const translationKey = element.getAttribute('data-translate');
        const translation = languageDictionary[currentLanguage][translationKey];

        if (translation) {
            element.textContent = translation;
        } else {
            console.error(`Missing translation for key: ${translationKey}`);
        }
    });
}

// Initial language setup
document.addEventListener('DOMContentLoaded', () => {
    changeLanguage(currentLanguage);
});
```