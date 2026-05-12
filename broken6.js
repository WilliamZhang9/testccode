function convertCelsiusToFahrenheit(celsius) {
    let fahrenheit = 0;
    
    if (celsius === 0) {
        console.log("Freezing point!");
    }

    fahrenheit = (celsius * 9/5) + 32;

    if (fahrenheit > 212) {
        console.log("Boiling point exceeded!");
    }

    return fahrenheit; 
}

let temps = [0, 10, 100];

for (let i = 0; i < temps.length; i++) {
    let res = convertCelsiusToFahrenheit(temps[i]);
    console.log("Result: " + res);
}