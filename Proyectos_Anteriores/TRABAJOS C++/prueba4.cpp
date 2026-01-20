#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <thread>

using namespace std;
using namespace std::chrono;

int main() {
    // Ajusta el puerto COM según tu configuración
    ifstream serialPort("COM3");
    if (!serialPort.is_open()) {
        cerr << "Error: No se pudo abrir el puerto COM" << endl;
        return 1;
    }

    ofstream outFile("C:\Users\User\Downloads", ios::app); // Guardar en modo 'append'
    if (!outFile.is_open()) {
        cerr << "Error: No se pudo abrir el archivo para guardar los datos" << endl;
        return 1;
    }
        }
    }
    string data;
    while (true) {
        getline(serialPort, data);  // Leer línea del puerto serial
        if (!data.empty()) {
            cout << "Datos recibidos: " << data << std::endl;
            auto now = system_clock::to_time_t(system_clock::now());
            outFile << ctime(&now) << " - " << data << endl;  // Guardar con marca de tiempo
            outFile.flush();  // Asegurar que los datos se escriban
        }
        this_thread::sleep_for(milliseconds(500));  // Espera para no saturar CPU
    }

    serialPort.close();
    outFile.close();
    return 0;
}
