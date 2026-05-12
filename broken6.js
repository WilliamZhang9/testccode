function convertCelsiusToFahrenheit(celsius) {
    let fahrenheit = 0;
    
    // Fixed: Changed assignment (=) to equality (===)
    if (celsius === 0) {
        console.log("Freezing point!");
    }

    fahrenheit = (celsius * 9/5) + 32;

    // Fixed: Added missing closing parenthesis
    if (fahrenheit > 212) {
        console.log("Boiling point exceeded!");
    }

    // Fixed: Corrected spelling from 'farenheit' to 'fahrenheit'
    return fahrenheit; 
}

let temps = [0, 10, 100];

// Fixed: Changed loop boundary from '<=' to '<' to avoid out-of-bounds access
for (let i = 0; i < temps.length; i++) {
    let res = convertCelsiusToFahrenheit(temps[i]);
    console.log("Result: " + res);
}
