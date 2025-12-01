int[] ListaCortaNum = {1, 2, 3, 4, 5};
Console.WriteLine(ListaCortaNum[4]);
List<int> ListaLargaNum = new List<int> {6, 7, 8, 9, 10};
Console.WriteLine(string.Join(" ", ListaLargaNum));

string[] ListaCortaText = {"Uno", "Dos", "Tres", "Cuatro", "Cinco"};
Console.WriteLine(ListaCortaText[4]);
List<string> ListaLargaText = new List<string> {"Seis", "Siete", "Ocho", "Nueve", "Diez"};
Console.WriteLine(string.Join(", ", ListaLargaText));

double lista = 3.5;
dynamic[] DatosMixtos = {"Texto", 67, true, lista};
Console.WriteLine(string.Join(" ,", DatosMixtos));

Dictionary<int, string> jugadores = new Dictionary<int, string>();
jugadores.Add(10, "Messi");
jugadores.Add(7, "Cristiano");
Console.WriteLine(jugadores[7]);

Dictionary<string, string> DatosPersonales = new Dictionary<string, string>();
DatosPersonales.Add("Jose", "Arroz");
DatosPersonales.Add("Maria", "Papa");
DatosPersonales.Add("Alejandra", "Mama");
DatosPersonales.Add("Angye", "Amor No Correspondido");
Console.WriteLine(DatosPersonales["Angye"]);

List<dynamic> DatosAngye2 = new List<dynamic> {};
DatosAngye2.Add(3144048151);
DatosAngye2.Add("Angye@gmail.com");
DatosAngye2.Add("Dg 49 sur");
List<dynamic> DatosKevin2 = new List<dynamic> {};
DatosKevin2.Add(3209813135);
DatosKevin2.Add("sugarrigbi@gmail.com");
DatosKevin2.Add("Dg 49 norte");
Dictionary<string, List<dynamic>> DatosPersonales2 = new Dictionary<string, List<dynamic>>();
DatosPersonales2.Add("Kevin Anzola", DatosKevin2);
DatosPersonales2.Add("Angye Mora", DatosAngye2);
Console.WriteLine("PRUEBA1");
Console.WriteLine(string.Join(" | ", DatosPersonales2["Kevin Anzola"]));
Console.WriteLine("PRUEBA2");
foreach (var item in DatosPersonales2)
{
    Console.WriteLine($"{item.Key}: {string.Join(" | ", item.Value)}");
}
Console.WriteLine("PRUEBA3");
Console.WriteLine(string.Join(" , ", DatosPersonales2.Keys));
Console.WriteLine("PRUEBA4");
Console.WriteLine(DatosPersonales2["Angye Mora"][1]);

Dictionary<string, string[]> Correos = new Dictionary<string, string[]>();
string[] CorreosAngye = {"Angye@outlook.com"};
Correos.Add("Angye Mora", CorreosAngye);
string[] CorreosKevin = {"Sugarrigbi@outlook.com", "kevinanzgarz26@outlook.com", "kmanzolag@outlook.com"};
Correos.Add("Kevin Anzola", CorreosKevin);
Console.WriteLine(Correos["Kevin Anzola"][2]);
Console.WriteLine(Correos);
Console.WriteLine(string.Join(" ,", Correos));
Console.WriteLine(Correos["Angye Mora"]);
