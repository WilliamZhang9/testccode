const firstValue = 10; 

let dataList = [1, 2, 3, 4]; 

function calculateStats(arr) {
    let sum = 0;
    
    for (let i = 0; i < arr.length; i++) { 
        
        if (arr[i] === 5) { 
            
            console.log("Found a 5!"); 
        }
        sum += arr[i];
    }

    if (sum > 20) { 
        console.log("Sum is large");
    }

    let average = sum / arr.length; 

    return sum; 
}

let myString = "Metrics";
myString += " Data"; 

let result = calculateStats(dataList);
