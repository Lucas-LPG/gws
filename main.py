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
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "cz/enviar"

sensor = dht.DHT22(Pin(15))

enter_button = Pin(25, Pin.IN, Pin.PULL_UP)
exit_button = Pin(26, Pin.IN, Pin.PULL_UP)
num_people = 0
movement_sensor = Pin(33, Pin.IN)
sg90 = PWM(Pin(22, mode=Pin.OUT))
sg90.freq(50)

print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Connected!")

def servo(movement_sensor):
    if movement_sensor == 1:
        sg90.duty(99)
    if movement_sensor == 0:
        sg90.duty(30)

prev_weather = ""

while True:
  print("Measuring weather conditions... ", end="")
  sensor.measure()
  servo(movement_sensor.value())

  message = ujson.dumps({
      "temperature": sensor.temperature(),
      "enterPeople": enter_button.value(),
      "exitPeople": exit_button.value()
  })

  if message != prev_weather:
      print("Updated!")
      print("Reporting to MQTT topic {}: {}".format(MQTT_TOPIC, message))
      client.publish(MQTT_TOPIC, message)
      prev_weather = message
  else:
      print("No change")

  time.sleep(0.1)

    
