/* 
Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um 
método acessor (get) e um método modificador (set) para cada. Defina um objeto 
para cada atributo e elabore um construtor para criar alguma regra.

A atividade pode ser realizada em qualquer linguagem de programação ou apenas 
utilizando algoritmos.
*/

//A CLASSE CRIADA FOI A CLASSE BANCO QUE ESTÁ DENTRO DESTE MESMO PACOTE

package poo_ativ06;

public class Banco {
	public String conta;
	public double saldo;
	
	
	
	public Banco(double saldo) {
		this.saldo = saldo;
	}
	public Banco(String conta) {
		this.conta = conta;
	}
	public String getConta() {
		return conta;
	}
	public void setConta(String conta) {
		this.conta = conta;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	
	@Override
	public String toString() {
		return "Banco [conta=" + conta + ", saldo=" + saldo + "]";
	}
	public static void main(String[] args) {
		Banco b1= new Banco("1233-67");
		b1.setSaldo(3000.00);
		Banco b2= new Banco(100.00);
		b2.setConta("111-3");
		
		System.out.println(b1);
		System.out.println(b2);
		
	}
	
	
}
