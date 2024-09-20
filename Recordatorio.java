package aed;

public class Recordatorio {
    private String m;
    private Fecha f;
    private Horario h;

    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        m = mensaje;
        f = fecha;
        h = horario;
    }

    public Horario horario() {
        return h;
    }

    public Fecha fecha() {
        return f;
    }

    public String mensaje() {
        return m;
    }

    @Override
    public String toString() {
        return m + "@" + f + h;
    }

    @Override
    public boolean equals(Object otro) {
        // Implementar
        return true;
    }

}
