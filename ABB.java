package aed;

import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> implements Conjunto<T> {
    private Nodo raiz;
    private int elementos;


    private class Nodo {
        T valor;
        Nodo der;
        Nodo izq;
        Nodo padre;

        public Nodo(T v) {
            padre = null;
            valor = v;
            der = null;
            izq = null;
        }
    }

    public ABB() {
        raiz = null;
        elementos = 0;
    }

    public int cardinal() {
        return elementos;
    }

    public T minimo(){
        Nodo minimo = raiz;
        if (raiz == null) {
            minimo = null;
        }
        else {
            while (minimo.izq != null) {
                minimo = minimo.izq;
            }public void insertar(T elem){
                Nodo nuevo = new Nodo(elem);
                Nodo actual = raiz;
                if (! pertenece(elem)) {
                    elementos ++;
                    while (actual != null) {
                        if ((elem.compareTo(actual.valor) > 0)) {
                            actual = actual.der;
                            
                        }
                        else {
                            actual = actual.izq;
                            
                        }
                    }
                    if (actual == null) {
                        actual = nuevo;
                    }
                }
            }
        }
        return minimo.valor;
    }

    public T maximo(){
        Nodo maximo = raiz;
        if (raiz == null) {
            maximo = null;
        }
        else {
            while (maximo.der != null) {
                maximo = maximo.der;
            }
        }
        return maximo.valor;
    }

    public void insertar2(T elem){
        Nodo nuevo = new Nodo(elem);
            if (! pertenece(elem)) {
                elementos ++;
                if (raiz == null) {
                    raiz = nuevo;
                }
                else {
                    Nodo actual = raiz;
                    while (actual.der != null || actual.izq != null) {
                        if (elem.compareTo(actual.valor) > 0) {
                            if (actual.der != null) {
                                actual = actual.der;
                            }
                            else {
                                actual.der = nuevo;
                                nuevo.padre = actual;
                                break;
                            }
                        }
                        else {
                            if (actual.izq != null) {
                                actual = actual.izq;
                            }
                            else {
                                actual.izq = nuevo;
                                nuevo.padre = actual;
                                break;
                            }
                        }
                    }
                    if (actual.der == null && actual.izq == null) {
                        if (elem.compareTo(actual.valor) > 0) {
                            actual.der = nuevo;
                            actual.der.padre = actual;
                        }
                        else {
                            actual.izq = nuevo;
                            actual.izq.padre = actual;
                        }
                    }
                }
            }
    }

    public void insertar(T elem){
        Nodo nuevo = new Nodo(elem);
        Nodo actual = raiz;
        if (! pertenece(elem)) {
            elementos ++;
            while (actual != null) {
                if ((elem.compareTo(actual.valor) > 0)) {
                    actual = actual.der;
                    
                }
                else {
                    actual = actual.izq;
                    
                }
            }
            if (actual == null) {
                actual = nuevo;
            }
        }
    }

    public boolean pertenece(T elem){
        Nodo actual = raiz;
        if (actual != null) {
            return false;
        }
        while (actual != null) {
            if (actual.valor == elem) {
                return true;
            }
            if (elem.compareTo(actual.valor) > 0) {
                actual = actual.der;
            }
            else {
                actual = actual.izq;
            }
        }
        return false;
    } 

    public void eliminar(T elem){
        throw new UnsupportedOperationException("No implementada aun");
    }

    public String toString(){
        throw new UnsupportedOperationException("No implementada aun");
    }

    private class ABB_Iterador implements Iterador<T> {
        private Nodo _actual;

        public boolean haySiguiente() {            
            throw new UnsupportedOperationException("No implementada aun");
        }
    
        public T siguiente() {
            throw new UnsupportedOperationException("No implementada aun");
        }
    }

    public Iterador<T> iterador() {
        return new ABB_Iterador();
    }

}
