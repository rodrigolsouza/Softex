/*
Crie dois pacotes baseados nas atribuições de uma empresa e inclua classes neles. 
Lembre-se de trabalhar com os padrões Java.
 */

package poo_ativ09_Package01;

public class Recrutar {
	int numFuncionarios;
	String cargo;
	DefinirSalario salario;
	
	
	public int getNumFuncionarios() {
		return numFuncionarios;
	}
	public void setNumFuncionarios(int numFuncionarios) {
		this.numFuncionarios = numFuncionarios;
	}
	public String getCargo() {
		return cargo;
	}
	public void setCargo(String cargo) {
		this.cargo = cargo;
	}
	public DefinirSalario getSalario() {
		return salario;
	}
	public void setSalario(DefinirSalario salario) {
		this.salario = salario;
	}

}
