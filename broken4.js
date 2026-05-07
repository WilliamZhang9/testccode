// broken_calc.js

function calculateTotal(items, taxRate) {
    let subtotal = 0;
    
    for (let i = 0; i < items.length; i++) {
        subtotal += items[i].price;
    }

    // Syntax Error: Missing closing parenthesis ')' in the if condition
    if (subtotal > 100 {
        console.log("Applying discount!");
        subtotal = subtotal * 0.9;
    }

    // Logic Error: If taxRate is passed as a string (e.g., "0.05"), 
    // (1 + "0.05") results in string concatenation ("10.05") rather than math (1.05)
    let finalTotal = subtotal * (1 + taxRate);
    return finalTotal;
}

const cart = [
    { name: "Book", price: 20 },
    { name: "Pen", price: 5 }
];

// Passing taxRate as a string triggers the logic error
console.log("Total is: " + calculateTotal(cart, "0.05"));