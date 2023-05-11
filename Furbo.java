package com.mycompany.furbo;

public class Furbo {

    public static void main(String[] args) {
        EquipoFurbo equipo = new EquipoFurbo("FC Barcelona");
        JugadorFutbol jugador1 = new JugadorFutbol("Messi",25);
        JugadorFutbol jugador2 = new JugadorFutbol("Suarez",30);
        equipo.AgregarPlayer(jugador1);
        equipo.AgregarPlayer(jugador2);
        
        equipo.ImprimirInfoJu();
    }
}
