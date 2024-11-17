#include <iostream>
using namespace std;

struct Nodo {
    string categoria;
    int movimientosRealizados;
    int recaudacionTotal = 0;
    int recaudacionActual;
    Nodo *siguiente;
};

Nodo *inicio = nullptr, *pilaTemporal = nullptr, *auxiliar = nullptr;

void agregarVehiculo() {
    auxiliar = (Nodo*) malloc(sizeof(Nodo));
    int tipoVehiculo;
    cout << "Ingrese el tipo de vehículo (1. Motocicleta, 2. Automóvil): ";
    cin >> tipoVehiculo;
    auxiliar->categoria = (tipoVehiculo == 1) ? "Motocicleta" : "Automóvil";
    auxiliar->movimientosRealizados = 0;
    auxiliar->recaudacionActual = 0;
    
    if (!inicio) {
        inicio = auxiliar;
        inicio->siguiente = nullptr;
    } else {
        auxiliar->siguiente = inicio;
        inicio = auxiliar;
    }
    auxiliar = nullptr;
}

void retirarVehiculo() {
    if (inicio == nullptr) {
        cout << "No hay vehículos estacionados." << endl;
        return;
    }

    cout << "Ingrese la cantidad de movimientos al retirar el vehículo: ";
    cin >> inicio->movimientosRealizados;

    int tarifaBase = (inicio->categoria == "Motocicleta") ? 1000 : 2000;
    int tarifaMovimientos = inicio->movimientosRealizados * 100;
    int montoFinal = tarifaBase + tarifaMovimientos;

    inicio->recaudacionTotal = montoFinal;

    cout << "El vehículo (" << inicio->categoria << ") fue retirado. Total a pagar: $" << montoFinal << endl;

    auxiliar = inicio;
    inicio = inicio->siguiente;
    free(auxiliar);
}

void mostrarRecaudacionTotal() {
    int totalAcumulado = 0;

    cout << "Recaudación acumulada por cada vehículo:" << endl;
    
    while (inicio != nullptr) {
        totalAcumulado += inicio->recaudacionTotal;
        cout << "Monto recaudado por el vehículo: $" << inicio->recaudacionTotal << endl;
        
        if (inicio == nullptr) {
            pilaTemporal = inicio;
            inicio = inicio->siguiente;
            pilaTemporal->siguiente = nullptr;
        } else {
            auxiliar = inicio;
            inicio = inicio->siguiente;
            auxiliar->siguiente = pilaTemporal;
            pilaTemporal = auxiliar;
            auxiliar = nullptr;
        }
    }

    while (pilaTemporal != nullptr) {
        if (inicio == nullptr) {
            inicio = pilaTemporal;
            pilaTemporal = pilaTemporal->siguiente;
            inicio->siguiente = nullptr;
        } else {
            auxiliar = pilaTemporal;
            pilaTemporal = pilaTemporal->siguiente;
            auxiliar->siguiente = inicio;
            inicio = auxiliar;
            auxiliar = nullptr;
        }
    }

    cout << "Recaudación total acumulada: $" << totalAcumulado << endl;
}

int main() {
    int opcion;

    do {
        cout << "- Menú de Estacionamiento -" << endl;
        cout << "1. Registrar vehículo" << endl;
        cout << "2. Retirar vehículo" << endl;
        cout << "3. Ver total recaudado" << endl;
        cout << "4. Salir del sistema" << endl;
        cout << "Elija una opción: ";
        cin >> opcion;

        switch(opcion) {
            case 1:
                agregarVehiculo();
                break;
            case 2:
                retirarVehiculo();
                break;
            case 3:
                mostrarRecaudacionTotal();
                break;
        }
    } while (opcion != 4);

    return 0;
}
