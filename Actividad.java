package com.mycompany.a;

public class Actividad {
    private String nombre;
    private int duracion;

    public Actividad(String nombre, int duracion) {
        this.nombre = nombre;
        this.duracion = duracion;
    }
    
    public void ImprimirInf(){
        System.out.println("Nombre: "+this.nombre);
        System.out.println("Duracion: "+this.duracion);
    }

    public int getDuracion() {
        return duracion;
    }
}
