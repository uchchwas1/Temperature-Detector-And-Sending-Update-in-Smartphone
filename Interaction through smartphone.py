from twilio.rest import Client
import serial
import time

ser = serial.Serial('COM4', 9600)
account_sid = 'AC542f2f603c93ea88afabcf31419d5d83'
auth_token = '1f32e1fd9595740d78e85c4ef945f760'
client = Client(account_sid, auth_token)
temp1 = 0

while True:
    while ser.inWaiting():
         temp = ser.readline().decode()
         if(temp!=temp1):
             temp1=temp
             messageTosend = "Alert!! The temp is " + temp + " Celsius"

             message = client.messages.create(
                body=messageTosend,
                from_='whatsapp:+14155238886',
                to='whatsapp:+8801785904633')
             print(message.sid)
    time.sleep(10)

# Optional Portion(Do not change it)

# temp = ser.readline().decode()
# print(temp)
#
# messageTosend = "Alert!! The temp is " + temp + " Celsius"

# message = client.messages.create(body=messageTosend, from_='whatsapp:+14155238886', to='whatsapp:+8801785904633')

# print(message.sid)