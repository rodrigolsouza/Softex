/*
Classifique dois objetos materiais e dois abstratos. Insira, no mínimo, três métodos e três atributos para cada.
*/

//abstrato: contaBancaria, Data
// material: pessoa, celular

/**********************************************ABSTRATOS*****************************************************
public class ContaBancaria{
    public String numeroConta;
    public  Double saldo;
    public String tipo;

    public void creditar(double valor){
        this.saldo+=valor
    }

    public void debitar(double valor){
        this.saldo-=valor
    }

    public double consultarSaldo(){
        return this.saldo;
    }
}

public class Data{
    public int dia;
    public int mes;
    public int ano;


    public int getDia(){
        return this.dia;
    }

    public void setMes( int valorMes){
        this.mes+=valorMes;
    }

    public int getDia(){
        return this.dia;
    }
}

*************************************MATERIAL****************************************************************
public class Pessoa{
    private String dataNascimento;
    private String nome;
    private String nacionalidade;

    public String getDataNascimento(){
        return this.dataNascimento;
    }

    pulic void imprimirPessoa(){
        System.out.printf(this.nome + this.nacionalidade + this.dataNascimento);
    }

    public void mudarNacionalidade(String novaNacionalidade){
        this.nacionalidade=novaNacionalidade;
    }
}

public class Celular{
    String numero;
    String modelo;
    Boolean estaligado=true;

    public void alterarNumero( String novoNumero){
        this.numero=novoNumero;
    }

    public void desligarCelular(){
        this.estaligado=false;
    }

    public String getModelo(){
        return this.Modelo;
    }
}

 */

