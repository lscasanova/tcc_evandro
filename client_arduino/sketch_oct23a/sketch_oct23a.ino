#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// usa IP estático se o DHCP falhar
IPAddress ip(192, 168, 0, 177);
IPAddress myDns(192, 168, 0, 1);

// Initializa a biblioteca Ethernet
EthernetClient client;

// Variaveis para medir a velocidade
unsigned long beginMicros, endMicros;
unsigned long byteCount = 0;
bool printWebData = true;

// Servidor para a consulta dos alunos
char server[] = "servidor-tcc.herokuapp.com";

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // Inicia a conexão Ethernet:
  Serial.println("Iniciando Ethernet com DHCP:");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Falha na configuracao Ethernet usando DHCP");
    // Verifica se o hardware Ethernet está presente
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("Ethernet shield nao encontrado. :(");
      while (true) {
        delay(1);
      }
    }
    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("cabo Ethernet nao conectado.");
    }
    // tenta configurar usando endereco IP ao inves de DHCP:
    Ethernet.begin(mac, ip, myDns);
  } else {
    Serial.print("  DHCP assigned IP ");
    Serial.println(Ethernet.localIP());
  }
  // espera um segundo para o Ethernet shield conectar:
  delay(1000);
  Serial.print("conectando... ");
  Serial.print(server);
  Serial.println("...");

  // Imprime detalhes da conexao:
  if (client.connect(server, 80)) {
    Serial.print("connected to ");
    Serial.println(client.remoteIP());
    // Make a HTTP request:
    client.println("GET /alunos HTTP/1.1");
    client.println("Host: servidor-tcc.herokuapp.com");
    client.println("Connection: close");
    client.println();
  } else {
    // if you didn't get a connection to the server:
    Serial.println("conexao falhou");
  }
  beginMicros = micros();
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  int len = client.available();
  if (len > 0) {
    byte buffer[80];
    if (len > 80) len = 80;
    client.read(buffer, len);
    if (printWebData) {
      Serial.write(buffer, len); // show in the serial monitor (slows some boards)
    }
    byteCount = byteCount + len;
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    endMicros = micros();
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    Serial.print("Received ");
    Serial.print(byteCount);
    Serial.print(" bytes in ");
    float seconds = (float)(endMicros - beginMicros) / 1000000.0;
    Serial.print(seconds, 4);
    float rate = (float)byteCount / seconds / 1000.0;
    Serial.print(", rate = ");
    Serial.print(rate);
    Serial.print(" kbytes/second");
    Serial.println();

    // do nothing forevermore:
    while (true) {
      delay(1);
    }
  }
}
