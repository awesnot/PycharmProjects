import paho.mqtt.climer as mqtt

def ao_conectar(client, userdata, flags, rc):
    print("Nos conectar com o seguine código de resultado {}".format (str(rc)))

def ao_receber(client, userdata, msg):
    print("{}---{}".format(msg.topic,str(mgs.payload)))
