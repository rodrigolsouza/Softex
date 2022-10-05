/*
Crie dois pacotes baseados nas atribuições de uma empresa e inclua classes neles. 
Lembre-se de trabalhar com os padrões Java.
 */

package poo_ativ09_Package01;

public class DefinirSalario {
	int salario;
	String codigoFuncionario;
	String cargo;
	
	
	public int getSalario() {
		return salario;
	}
	public void setSalario(int salario) {
		this.salario = salario;
	}
	public String getCodigoFuncionario() {
		return codigoFuncionario;
	}
	public void setCodigoFuncionario(String codigoFuncionario) {
		this.codigoFuncionario = codigoFuncionario;
	}
	public String getCargo() {
		return cargo;
	}
	public void setCargo(String cargo) {
		this.cargo = cargo;
	}
}
