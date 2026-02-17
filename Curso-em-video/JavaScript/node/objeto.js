/** Estrutura simples de um Objeto */
let amigo = {
  nome: "Lívia",
  sexo: "F",
  altura: 64.7,
  crecer(p = 0) {
    console.log("creceu");
    this.altura += p; /** altera o valor do indice "altura" do objeto "amigo" */
  },
}; 
amigo.crecer(1); /*chama a funsão e executa-la*/
console.log(amigo.nome); /** mostra o valor "nome" do indice "amigo" */
console.log(`${amigo.nome} tem ${amigo.altura} cm, Incrível!!`);
