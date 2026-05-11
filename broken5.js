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

    let totalWithTax = totalAmnt * (1 + taxRate); 
    console.log("Total is: " + totalWithTax); 

    return totalAmnt;
}

processCart([{name: "Apple", price: 50}, {name: "Banana", price: 20}]);