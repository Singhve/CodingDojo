//Predict 1: 

for(var num = 0; num < 15; num++){
    console.log(num);
}
//Prints 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14

//Predict 2:

for(var i = 1; i < 10; i+=2){
    if(i % 3 == 0){
        console.log(i);
    }
}
//vairbale = 1: 1%3  remainder = 1
//variable = 3: 3%3  remainder = 0; concssole.log(3)
//variable = 5: 5%3  remainder = 2;
//variable = 7: 7%3  remainder = 1;
//variable = 9: 9%3  remainder = 0; console.log(9)
//Prints: 3,9

//Predict 3:
for(var j = 1; j <= 15; j++){
    //If we Divive by 2 will the remainder be 0, if yes add 2 to J
    if(j % 2 == 0){
        j+=2;
    }
    //only do this if the first 'IF' isnt true
    //If we Divive by 3 will the remainder be 0, if yes add 1 to J 
    else if(j % 3 == 0){
        j++;
    }

   console.log(j);
}

//Prints: 1,4,5,8,10,11,14,16
