package aed;

public class Horario {
    private Integer h;
    private Integer m;

    public Horario(int hora, int minutos) {
        h = hora;
        m = minutos;
    }

    public int hora() {
        return h;
    }

    public int minutos() {
        return m;
    }

    @Override
    public String toString() {
        return h + ":" + m;
    }

    @Override
    public boolean equals(Object otro) {
        boolean otroEsNull = (otro == null);
        boolean claseDistinta = otro.getClass() != this-getClass();
        if (otroEsNull || claseDistinta){
            return false;
        }
        Horario otroComoHorario = (Horario)otro;
        return otroComoHorario.hora() == h && otroComoFecha.minutos() == m;
    }

}
