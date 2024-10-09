import random
import time
from temp_proco_linux import get_cpu_temperature


from paho.mqtt import client as mqtt_client

# --------------------------------------------------

broker = 'test.mosquitto.org'
login = ''
password = ''
port = 1883
topic = "/foo"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

# --------------------------------------------------

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(login, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# --------------------------------------------------

def publish(client):
    time.sleep(1)
    msg = get_cpu_temperature()
    result = client.publish(topic, msg)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

# --------------------------------------------------

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

# --------------------------------------------------

if __name__ == '__main__':
    run()

# --------------------------------------------------
