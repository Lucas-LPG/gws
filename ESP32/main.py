"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""

import network
import time
from machine import Pin, PWM
import dht
import ujson
from umqtt.simple import MQTTClient

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo2000"
MQTT_BROKER = "mqtt-dashboard.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "cz/enviar"
MQTT_TOPIC_RECIVE = "cz/receba"

sensor = dht.DHT22(Pin(15))

enter_button = Pin(25, Pin.IN, Pin.PULL_UP)
exit_button = Pin(26, Pin.IN, Pin.PULL_UP)
num_people = 0
movement_sensor = Pin(33, Pin.IN)
Ar_condicionado = Pin(23, Pin.OUT)
porta = PWM(Pin(22, mode=Pin.OUT))
janela = PWM(Pin(27, mode=Pin.OUT))
porta.freq(50)
janela.freq(60)

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER,
                    user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Connected!")


def servo(enter_button, exit_button):
    global num_people
    if enter_button == 0 and num_people < 100:
        porta.duty(99)
        num_people += 1
        print(num_people)
        time.sleep(1)
        porta.duty(30)
    elif exit_button == 0 and num_people < 100:
        porta.duty(99)
        num_people -= 1
        print(num_people)
        time.sleep(1)
        porta.duty(30)
    elif num_people >= 100:
        porta.duty(30)


prev_weather = ""


def handle_message(topic, msg):
    string = msg.decode()
    string_limpa = string.replace('{', '').replace('}', '')
    partes = string_limpa.split(':')
    numero = partes[1].strip()
    print(numero)
    if numero == '"1"':
        Ar_condicionado.value(1)
        janela.duty(30)
    else:
        Ar_condicionado.value(0)
        janela.duty(90)


client.set_callback(handle_message)
client.subscribe(MQTT_TOPIC_RECIVE)


def check_connection(client):

    try:

        client.ping()
    except OSError as e:
        if e.args[0] == 104:  # ECONNRESET
            print("A conexão com o broker MQTT foi interrompida. Tentando reconectar...")
            client.connect()


while True:
    client.check_msg()
    check_connection(client)
    print("Measuring weather conditions... ", end="")

    sensor.measure()

    message = ujson.dumps({
        "temperature": sensor.temperature(),
        "enterPeople": enter_button.value(),
        "exitPeople": exit_button.value()
    })

    if message != prev_weather:
        print("Updated!")
        print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
        check_connection(client)
        client.publish(MQTT_TOPIC, message)
        servo(enter_button.value(), exit_button.value())
        prev_weather = message
    else:
        print("No change")

    time.sleep(1)
