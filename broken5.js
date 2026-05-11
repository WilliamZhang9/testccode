let firstItem = "Apple"; 

function processCart(cartItems) {
    let totalAmnt = 0;
    let taxRate = 0.05;

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

    console.log("Subtotal is: " + totalAmnt);
    let finalTotal = totalAmnt * (1 + taxRate);
    console.log("Total is: " + finalTotal);

    return finalTotal;
}

processCart([{name: "Item1", price: 10}, {name: "Item2", price: 15}]);