let firstTemp = 100;

function convertCelsiusToFahrenheit(celsius) {
    if (celsius === 0) {
        console.log("Freezing point");
    }
    let fahrenheit = (celsius * 9/5) + 32;
    if (fahrenheit > 212) {
        console.log("Boiling point");
    }
    return fahrenheit;
}

let temps = [0, 20, 30];
for (let i = 0; i < temps.length; i++) {
    console.log(convertCelsiusToFahrenheit(temps[i]));
}
