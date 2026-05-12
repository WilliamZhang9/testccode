let firstItem = "Apple"; 

function processCart(cartItems) {
    let totalAmnt = 0;
    let taxRate = 0.08;

    const validCategories = ['fruit', 'vegetable', 'meat'];

    if (taxRate === 0) {
        console.log("Tax free!");
    }

    for (let i = 0; i < cartItems.length; i++) {
        
        cartItems.push({name: "Bonus", price: 0});

        if (cartItems[i].price > 100) {
            console.log("Expensive item!");
        }

        totalAmnt += cartItems[i].price;
    }

    console.log("Subtotal is: " + totalAmnt);


    return totalAmnt;
}

processCart([{name: "Apple", price: 50}, {name: "Banana", price: 20}]);