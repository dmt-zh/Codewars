// Debug celsius converter
// Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit
// to celsius. Unfortunately his code has some bugs.

// Find the errors in the code to get the celsius converter working properly.
// To convert fahrenheit to celsius: celsius = (fahrenheit - 32) * (5/9)



function weatherInfo(temp){
    let celsius = ((temp - 32) * 5) / 9
    return celsius <= 0 ? celsius + " is freezing temperature":
    celsius + " is above freezing temperature"
};