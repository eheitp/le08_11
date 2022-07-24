import paho.mqtt.client as mqtt
import django
django.setup()
from .models import *

def on_connect(client, userdata, flags, rc):
    #print("Connected with result code " + str(rc)) #notify about established connection
    client.subscribe("message")

def on_message(client, userdata, msg):
    ms = msg.payload
    data = str(ms[0: len(ms)])[2:-1]
    print("Your message:" + data) #display received message
    ss = data.split(' ')
    temp = ss[0]
    hum = ss[1]
    print("temp :" + str(temp))
    print("hum :" + str(hum))
    s=Dht.objects.create(temp=temp, hum=hum)
    #x=Dht.objects.last()
    #print("x")
    #print(x)
    #groups = Dht.objects.create()
    #client.disconnect()

client = mqtt.Client()

''' replace with username for authentification '''
client.username_pw_set("user","user")

''' connect with EC2 instance through encrypted port 8883 '''
#client.connect("broker.hivemq.com", 1883, 60)
#client.connect("192.168.43.1", 1883, 60)
client.connect("mqtt.eclipseprojects.io", 1883, 60)
try:
    client.on_connect = on_connect
    client.on_message = on_message
#client.loop_forever() #do not disconnect
    client.loop_stop()
except Exception as e:
    print(e)
    pass