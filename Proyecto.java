package com.mycompany.a;
import java.util.ArrayList;
import java.util.List;

public class Proyecto {
    private String nombre;
    private List<Actividad> actividades;

    public Proyecto(String nombre) {
        this.nombre = nombre;
        this.actividades = new ArrayList<>();
    }
    
    public void agregarActividad(String nombre, int duracion){
        Actividad activ = new Actividad(nombre,duracion);
        this.actividades.add(activ);
    }
    
    public void DuracionTotal(){
        int Dtotal =0;
        for(Actividad actividad : this.actividades){
            Dtotal += actividad.getDuracion();
        }
        System.out.println("Duracion del proyecto "+this.nombre+": "+ Dtotal);
    }
    
    public List<Actividad> getActividades(){
        return this.actividades;
    }
}
