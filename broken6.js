function convertCelsiusToFahrenheit(celsius) {
    if (celsius === 0) {
        console.log("Freezing point of water reached.");
    }
    let fahrenheit = (celsius * 9/5) + 32;
    return fahrenheit;
}

let temp1 = 100;
let temps = [0, 20, 30, temp1];

for (let i = 0; i < temps.length; i++) {
    let f = convertCelsiusToFahrenheit(temps[i]);
    if (f > 212) {
        console.log("Above boiling point!");
    }
}
