
package poo_ativ09_Package02;

import poo_ativ09_Package01.*;

public class CalcularReceita {
	Recrutar rec= new Recrutar();
	double preçoProduto;
	double quantProdVendidosPorFuncionario;
	
	public double CalcularTotalVendido() {
		return this.quantProdVendidosPorFuncionario*rec.getNumFuncionarios();
	}
	public double CalcularReceitaTotal() {
		return this.CalcularTotalVendido()*preçoProduto;
	
	}
}
