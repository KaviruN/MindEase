const inputs = document.querySelectorAll('.verify__inputs--num');

inputs.forEach((input, index) => {
    input.addEventListener('input', () => {
        if (input.value.length === 1 && index < inputs.length - 1) {
            inputs[index + 1].focus();
        }
    });

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Backspace' && input.value.length === 0 && index > 0) {
            inputs[index - 1].focus();
        }
    });

    input.addEventListener('paste', (e) => {
        e.preventDefault();
        const pasteData = e.clipboardData.getData('text').split('');
        pasteData.forEach((char, i) => {
            if (inputs[index + i]) {
                inputs[index + i].value = char;
            }
        });
        const nextInput = inputs[index + pasteData.length];
        if (nextInput) {
            nextInput.focus();
        }
    });
});