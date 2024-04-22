//Exemplo 1:
void main() {
  String nome = "Vitor";
  String sobNome = "Sauer";
  
  print('$nome $sobNome');
  
}

//Exemplo 2:

void main(){
  cadastrarUsuario('Alberto', 'Poems');
}

void cadastrarUsuario (String? name, String? sobrenome){
  if (name != null){
    print(name);
  }
  
  if(sobrenome != null){
    print(sobrenome);
  }
  
  String nomeCompleto = sobrenome ?? 'Usuario Desconhecido';
  print(nomeCompleto);
}

