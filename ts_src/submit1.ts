console.log('Hello, this is submit1.');

function setValidation(fieldId: string, feedbackId: string, isValid: boolean, text?: string) {
    const fieldElement = document.getElementById(fieldId);
    const feedbackElement = document.getElementById(feedbackId);

    if (!fieldElement) {
        console.log(`Field ID ${fieldId} does not exist.`);
        return;
    }

    if (!feedbackElement) {
        console.log(`Feedback ID ${feedbackId} does not exist.`);
        return;
    }
    feedbackElement.textContent = text ? text : '';
    feedbackElement.className = isValid ? 'valid-feedback' : 'invalid-feedback';
    if (isValid) {
        // no problem even if is-invalid does not exist, in this case, do nothing
        fieldElement.classList.remove('is-invalid');
        fieldElement.classList.add('is-valid');
    } else {
        fieldElement.classList.remove('is-valid');
        fieldElement.classList.add('is-invalid');
    }
}

const field1 = document.getElementById('field1') as HTMLInputElement;
function validateField1(updateStyle: boolean): boolean {
    const fieldValue = field1.value;
    const isValid = fieldValue.length > 0 && fieldValue.length < 6;
    if (updateStyle) {
        setValidation('field1', 'field1Feedback', isValid, 
            isValid ? 'Valid.' : 'The length should be 1 to 5.');
    }
    return isValid;
}

const field2 = document.getElementById('field2') as HTMLInputElement;
function validateField2(updateStyle: boolean): boolean {
    const fieldValue = field2.value;
    const isValid = fieldValue.length > 0 && fieldValue.length < 3;
    if (updateStyle) {
        setValidation('field2', 'field2Feedback', isValid,
            isValid ? undefined : 'The length should be 1 or 2.');
    }
    return isValid;
}

const submitButton = document.getElementById('submitButton') as HTMLButtonElement;

const allFieldsAndValidateFunctions = new Map([
    [field1, validateField1],
    [field2, validateField2]
]);

function validateForm(idForUpdateStyle: string) {
    let allValid = true;
    // the order is 'value, key'
    allFieldsAndValidateFunctions.forEach((validateFunction, field) => {
        const isValid = validateFunction(idForUpdateStyle === field.id);
        if (!isValid) {
            allValid = false;
        }
    })
    submitButton.disabled = !allValid;
}

// check all fields when any of those fields is modified
allFieldsAndValidateFunctions.forEach((_validateFunction, field) => {
    field.addEventListener('input', () => { validateForm(field.id) });
    field.addEventListener('blur', () => { validateForm(field.id) });
})
