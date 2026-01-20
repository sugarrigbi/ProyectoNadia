#include <iostream> //Imprimir en consola, gestionar salida y entrada de datos
#include <fstream> //leer y escribir archivos
#include <string>  //permite manejar cadenas de texto
#include <chrono> //funcionalidades de tiempo (hora o fecha)
#include <thread> //permite usar hilos y retrasos en el programa

using namespace std;
using namespace std::chrono; //permite mas facilidad al usar chronos

int main() {
//Abrir puerto COM
    ifstream serialPort("COM3");
    if (!serialPort.is_open()) {
        cout << "Error: No se pudo abrir el puerto COM" << endl;
        return 1;
    }

    ofstream outFile("C:\\Users\\User\\Downloads\\datos_arduino.txt", ios::app); //permite abrir el archivo, el modo ios::app permite agregar datos al final sin sobreescribir el archivo
    if (!outFile.is_open()) { //si el codigo no se puede abrir dara este error
        cout << "Error: No se pudo abrir el archivo para guardar los datos" << endl;
        return 1;
    }
    string data; //Blucle infinito para guardar datos
    auto lastWriteTime = system_clock::now(); //referencia del tiempo actual
    while (true) {
        getline(serialPort, data);  // Leer línea del puerto serial
        if (!data.empty()) {
            cout << "Datos recibidos: " << data << std::endl;

            auto now = system_clock::now();
            auto duration = duration_cast<minutes>(now - lastWriteTime);

            if (duration.count() >= 1) {  // Si han pasado 1 minutos
                outFile << ctime(&now) << " - " << data << endl;  // Guardar datos con timestamp
                outFile.flush();  // Asegurar que se escriban los datos
                lastWriteTime = now;  // Actualizar el tiempo de la última escritura
            }            
            outFile.flush();  // Asegurar que los datos se escriban
        }
        this_thread::sleep_for(milliseconds(500));  // Espera para no saturar CPU
    }

    serialPort.close();
    outFile.close();
}
