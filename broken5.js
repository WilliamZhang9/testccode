let firstItem = "Apple";

function processCart(cartItems) {
    let totalAmnt = 0;
    let taxRate = 0.08;

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

    return totalAmnt;
}
