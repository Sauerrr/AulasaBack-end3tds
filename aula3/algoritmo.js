let pessoa = {
    idade: 17,
    cnh: false,
    autorizacao: true
}

if (pessoa.idade >= 18 && pessoa.cnh == true && pessoa.autorizacao == true){
    console.log("Voce ta liberado meu querido")
}else if (pessoa.idade >= 18 && pessoa.cnh == false && pessoa.autorizacao == true || pessoa.idade < 18 && pessoa.autorizacao == true){
    console.log("Autorizado, mas não pode dirigir")
}else if (pessoa.idade >=18 && pessoa.cnh == true && pessoa.autorizacao == false){
    console.log("Não autorizado, mas pode dirigir")
}else{
    console.log("Não esta autorizado, não pode dirigir ou é menor de 18 anos.")
}

