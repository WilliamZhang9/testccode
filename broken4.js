// broken_calc.js

function calculateTotal(items, taxRate) {
    let subtotal = 0;
    
    // Ensure taxRate is a number for arithmetic operations
    taxRate = parseFloat(taxRate);

    for (let i = 0; i < items.length; i++) {
        subtotal += items[i].price;
    }

    // Syntax Error Fixed: Added closing parenthesis ')'
    if (subtotal > 100) {
        console.log("Applying discount!");
        subtotal = subtotal * 0.9;
    }

    // Logic Error Fixed: taxRate is now a number, ensuring correct addition
    let finalTotal = subtotal * (1 + taxRate);
    return finalTotal;
}

const cart = [
    { name: "Book", price: 20 },
    { name: "Pen", price: 5 }
];

// Passing taxRate as a string, but it's handled correctly inside the function
console.log("Total is: " + calculateTotal(cart, "0.05"));
