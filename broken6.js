function convertCelsiusToFahrenheit(celsius) {
    let fahrenheit = (celsius * 9/5) + 32;
    if (celsius === 0) { // Fixed: Assignment (=) changed to equality (===)
        console.log("Freezing point of water reached.");
    }
    return fahrenheit; // Fixed: Corrected spelling from 'farenheit' to 'fahrenheit'
}

let firstTemp = 100; // Fixed: Variable name cannot start with a digit
if (firstTemp > 212) { // Fixed: Added missing closing parenthesis
    console.log("Above boiling point.");
}

const temps = [0, 10, 20, 30];
for (let i = 0; i < temps.length; i++) { // Fixed: Changed <= to < to avoid out-of-bounds error
    console.log(convertCelsiusToFahrenheit(temps[i]));
}
