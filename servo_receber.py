import paho.mqtt.client as mqtt
import time

# Configura莽茫o MQTT
MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_TOPIC_SEND = "cz/enviar_duty"
MQTT_TOPIC_RECEIVE = "cz/enviar"

# Callback executado quando uma mensagem MQTT 茅 recebida


def on_message(client, userdata, message):
    print("DISTANCIA: ", message.payload.decode())
    distance = float(message.payload.decode())
    duty = 0
    if distance >= 20 and distance <= 50:
        duty = 70
    elif distance > 50:
        duty = 100
    elif distance < 20:
        duty = 45

    client.publish(MQTT_TOPIC_SEND,
                   f'{duty}')


# Configura莽茫o do cliente MQTT
client = mqtt.Client("lucas_gasperin")
client.on_message = on_message

# Conex茫o ao broker MQTT e subscri莽茫o aos t贸picos
client.connect(MQTT_BROKER)
client.subscribe(MQTT_TOPIC_RECEIVE)

# Loop principal para receber mensagens MQTT
# client.loop_forever()


# Caso eu queria algo semelhante ao while true da ESP32
while True:
    client.loop(timeout=0.1)
