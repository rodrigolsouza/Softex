/* 
Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. 
Depois, desenvolva três ou mais objetos para testar o código.
*/
package POO_ativ04;

public class Pessoa{
    public String nome;
    public String nacionalidade;
    private double renda=1000;

    public double getRenda() {
        return this.renda;
    }
    public void atualizarRenda(double adicional) {
        this.renda += adicional;
    }
    public Pessoa(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }
    public String getNome(){
        return this.nome;
    }
    public String setNome(String novoNome){
        return this.nome=novoNome;
    }

    public void imprimirPessoa(){
        System.out.printf(this.nome + this.nacionalidade + this.getRenda());
    }

    public void mudarNacionalidade(String novaNacionalidade){
        this.nacionalidade=novaNacionalidade;
    }

    public void printString(){
        System.out.printf(" Nome: %s\n nacionalidade: %s\n Renda: %.2f\n" , this.getNome(), this.nacionalidade, this.getRenda());

    }


public static void main(String[] args){
    Pessoa p1=new Pessoa("brasileiro");
    Pessoa p2=new Pessoa("americano");
    Pessoa p3= new Pessoa("alemão");

    p1.setNome("Rodrigo");
    p1.printString();
    p1.atualizarRenda(200);
    p1.printString();

    p2.setNome("Maria");
    p2.printString();
    p2.mudarNacionalidade("inglesa");
    p2.printString();

    p3.setNome("João");
    p3.printString();
}
}
