package com.mycompany.furbo;

public class JugadorFutbol {
    private String nombre;
    private int edad;

    public JugadorFutbol(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    } 
    
    public void ImprimirInfo(){
        System.out.println("Nombre: "+this.nombre);
        System.out.println("Edad: " + this.edad);
    }
}
