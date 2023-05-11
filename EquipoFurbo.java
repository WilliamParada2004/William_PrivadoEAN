package com.mycompany.furbo;
import java.util.ArrayList;
import java.util.List;

public class EquipoFurbo {
    private String nombre;
    private List<JugadorFutbol> players;

    public EquipoFurbo(String nombre) {
        this.nombre = nombre;
        this.players = new ArrayList<>();
    }
    
    public void AgregarPlayer(JugadorFutbol jugador){
        this.players.add(jugador);
    }
    
    public void ImprimirInfoJu(){
        System.out.println("Jugadores del equipo "+ this.nombre+": ");
        for(JugadorFutbol jugador: this.players){
            jugador.ImprimirInfo();
        }
    }
}
