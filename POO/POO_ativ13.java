/*
 Crie um exemplo de como funcionam a serialização e a desserialização de um 
 sistema qualquer. Utilize as classes, os objetos e métodos padrões da Java e 
 insira um endereço físico fictício.
 */


import java.io.*;
  
class exemplo implements java.io.Serializable
{
    public int a;
    public String b;
  
    // Construtor padrão
    public exemplo(int a, String b)
    {
        this.a = a;
        this.b = b;
    }
  
}
  
class Teste
{
    public static void main(String[] args)
    {   
        exemplo object = new exemplo(1, "Rodrigo");
        String filename = "file.ser";
          
        // Serialição 
        try
        {   
            //Salvando o objeto no arquivo
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);
              
            // serialização do objeto
            out.writeObject(object);
              
            out.close();
            file.close();
              
            System.out.println("Objeto serializado com sucesso!");
  
        }
          
        catch(IOException ex)
        {
            System.out.println("Excessão");
        }
  
  
        
        
        exemplo object1 = null;
        // Desserialização
        try
        {   
            // Lendo o objeto do arquivo
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);
              
            //Desserialização do objeto
            object1 = (exemplo)in.readObject();
              
            in.close();
            file.close();
              
            System.out.println("Objeto foi desserializado");
            System.out.println("a = " + object1.a);
            System.out.println("b = " + object1.b);
        }
          
        catch(IOException ex)
        {
            System.out.println("Excessão da desserialização");
        }
          
        catch(ClassNotFoundException ex)
        {
            System.out.println("Excessão de classe não encontrada");
        }
  
    }
}