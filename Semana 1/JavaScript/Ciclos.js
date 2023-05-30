//While
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log('Fin del ciclo while');

//do while
//se ejecuta el codigo y luego se revisa la condición
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log('Fin del ciclo do while');

//for
for( let contando = 0; contando < 3; contando++){
    console.log(contando);
}
console.log('Fin del ciclo for');

// Palabra reservada: break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra todos los pares
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer nº par")

//Palabra reservada: continue
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue;//ir a la siguiente iteración
    }// Cada que comprueba que lo anterior es falso continua a console..
    console.log(contando); 
}
console.log("Termina el ciclo");

//Palabra reservada: continue y Etiquetas Labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio;//ir a la siguiente iteración
    }// Cada que comprueba que lo anterior es falso continua a console..
    console.log(contando); 
}
console.log("Termina el ciclo");

//Palabra reservada: continue y Etiquetas Labels
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio;//ir a la siguiente iteración
    }// Cada que comprueba que lo anterior es falso continua a console..
    console.log(contando); 
}
console.log("Termina el ciclo");