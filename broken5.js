let firstItem = "Apple";

function processCart(cartItems) {
    let totalAmount = 0;
    let taxRate = 0.05; // Corrected as per expected behavior

    const validCategories = ['fruit', 'vegetable', 'meat']; // Missing closing bracket

    if (taxRate === 0) { // Changed assignment to comparison
        console.log("Tax free!");
    }

    for (let i = 0; i < cartItems.length; i++) { // Corrected loop condition

        // Removed the problematic line that modifies the array during iteration:
        // cartItems.push({name: "Bonus", price: 0});

        if (cartItems[i].price > 100) { // Missing closing parenthesis
            console.log("Expensive item!");
        }

        totalAmount += cartItems[i].price; // Corrected variable name
    }

    console.log("Subtotal is: " + totalAmount); // Corrected variable name

    // Removed unused and problematic line:
    // let errorArray = new Array(-1);

    const finalTotal = totalAmount * (1 + taxRate); // Added tax calculation
    console.log("Total is: " + finalTotal.toFixed(2)); // Added final output, fixed to 2 decimal places

    return finalTotal; // Return final total
}

// Adjusted input to match expected subtotal of 25
processCart([{name: "Orange", price: 10}, {name: "Grape", price: 15}]);