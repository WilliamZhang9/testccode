let firstTemp = 100;

function convertCelsiusToFahrenheit(celsius) {
    let fahrenheit = 0;
    
    // Fixed: Use === for comparison instead of = for assignment
    if (celsius === 0) {
        console.log("Freezing point!");
    }

    fahrenheit = (celsius * 9/5) + 32;

    // Fixed: Added missing closing parenthesis
    if (fahrenheit > 212) {
        console.log("Boiling point exceeded!");
    }

    // Fixed: Corrected spelling of fahrenheit
    return fahrenheit; 
}

let temps = [0, 10, 100];

// Fixed: Changed <= to < to avoid out-of-bounds access
for (let i = 0; i < temps.length; i++) {
    let res = convertCelsiusToFahrenheit(temps[i]);
    console.log("Result: " + res);
}
