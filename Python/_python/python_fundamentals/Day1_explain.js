function reverseString(stringInput) {
    //create a new string to store the reverse in (have a variable for it)
    var newString = "";
    //for loop that starts from the end of the string until it gets to the beginnign of the string
    //each character we see in each iteration of the for loop, we put that character into our new string
    for (var i = stringInput.length - 1; i >= 0; i--) {
        // newString = newString + stringInput[i];
        newString += stringInput[i];
    }
    // return that new string 
    //console.log(newString)
    return newString;
}


console.log(reverseString("potato"))
console.log(reverseString("batman"))
console.log(reverseString("wonderwoman"))