let firstItem = "Apple";

const validCategories = ['fruit', 'vegetable', 'meat'];

let taxRate = 0.08;
if (taxRate === 0) {
    console.log("Tax-free zone!");
}

let cartItems = [
    { name: "Apple", price: 1.2 },
    { name: "Steak", price: 15.0 }
];

let totalAmnt = 0;

for (let i = 0; i < cartItems.length; i++) {
    totalAmnt += cartItems[i].price;
    
    if (cartItems[i].price > 100) {
        cartItems.push({ name: "Bonus", price: 0 });
    }
}

console.log("Subtotal is: " + totalAmnt);

let errorArray = new Array(0);
