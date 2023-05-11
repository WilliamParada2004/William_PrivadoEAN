package com.mycompany.a;
public class A {

    public static void main(String[] args) {
        Proyecto proyect = new Proyecto("Desarrollo de software");
        proyect.agregarActividad("Analisis de requerimientos", 10);
        proyect.agregarActividad("Diseño de la solucion", 20);
        proyect.DuracionTotal();
        for(Actividad actividad : proyect.getActividades()){
            actividad.ImprimirInf();
        }
    }
}
