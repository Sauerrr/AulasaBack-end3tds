//São exemplos diferentes do mesmo código.
void main (){
  isAuthorized("Vitor gatão");
}

void isAuthorized(String nome){
  List<String> auth = ["Vitor gatão", "vini feio", "Barrola bolas"];
  if(auth.contains(nome)){
    print("Autorizado");
  }else{
    print("Não autorizado");
  }
}


//Aqui a variável não pode ser nula
void main (){
  isAuthorized("Vitor gatão", 18);
}

void main (){
  isAuthorized("Vitor gatão", 18);
}
void isAuthorized(String nome, int? idade){
  List<String> auth = ["Vitor gatão", "vini feio", "Barrola bolas"];
  if(idade != null && auth.contains(nome) && idade >= 18){
    print("Autorizado");
  }else{
    print("Não autorizado");
  }
}

//Exemplo de variavel não nula tambem.
void main (){
  isAuthorized("Vitor gatão", idade: 18);
}

void isAuthorized(String nome, {int? idade}) {
  List<String> auth = ["Vitor gatão", "vini feio", "Barrola bolas"];
  if(idade != null && auth.contains(nome) && idade >= 18){
    print("Autorizado");
  }else{
    print("Não autorizado");
  }
}

//Exemplo de saudação:
void main(){
  salute(name : "Pedo sujo",sep: "*", age: 98);
}

void salute({
  required String name,
  String? sep,
  int? age
}) {
  print("Saudação do ${name}");
  if (sep != null){
    print(sep * 25);
  }
  if(age != null){
    print(age);
  }
  print(DateTime.now());
}