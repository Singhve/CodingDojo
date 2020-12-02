function reverseString(stringInput) {
    var newString = "";
    for (var i = stringInput.length - 1; i >= 0; i--) {
        newString += stringInput[i]
    }
    console.log(newString)
    return (newString)
}
reverseString("potato")
reverseString("batman")
reverseString("wonderwoman")