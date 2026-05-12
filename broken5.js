let firstItem = "Apple"; 

function processCart(cartItems) {
    let totalAmnt = 0;
    let taxRate = 0.08;

    const validCategories = ['fruit', 'vegetable', 'meat'];

    if (taxRate === 0) {
        console.log("Tax free!");
    }

    for (let i = 0; i < cartItems.length; i++) {
        if (cartItems[i].price > 100) {
            console.log("Expensive item!");
        }

        totalAmnt += cartItems[i].price;
    }
    
    // Fixed Issue 5: Corrected method name and moved outside loop to avoid infinite loop
    cartItems.push({name: "Bonus", price: 0});

    console.log("Subtotal is: " + totalAmnt);

    return totalAmnt;
}

let errorArray = [];
processCart([{name: "Apple", price: 50}, {name: "Banana", price: 20}]);
