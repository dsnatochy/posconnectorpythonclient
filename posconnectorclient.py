import socket, ssl, pprint
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='10.1.1.98'
port=60000

# require a certificate from the server
ssl_sock = ssl.wrap_socket(s,
                keyfile="client_key_nopass.pem",
                certfile="clientcert.pem",
                ca_certs="servercert.pem",
                cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect((host, port))

#print repr(ssl_sock.getpeername())
#print ssl_sock.cipher()
#print pprint.pformat(ssl_sock.getpeercert())

ssl_sock.write("{ \"referenceId\":\"myRefId_12342\", \"authzOnly\": true, \"amount\": 1000, \"tipAmount\": 0, \"disableTip\": false, \"authzOnly\": false, \"multiTender\":true, \"currency\":\"USD\", \"order\": { \"orderNumber\": \"123\", \"amounts\": { \"subTotal\":2000, \"discountTotal\": -1200, \"taxTotal\": 200, \"currency\": \"USD\" }, \"items\": [ { \"sku\": \"12345\", \"unitPrice\": 100, \"tax\": 100, \"discount\": -500, \"quantity\":10, \"unitOfMeasure\":\"EACH\", \"clientNotes\": \"any special instructions from client\", \"status\":\"ORDERED\", \"name\":\"Mini scone\" }, { \"sku\": \"54321\", \"unitPrice\": 200, \"tax\": 100, \"discount\": -500, \"quantity\":5, \"unitOfMeasure\":\"EACH\", \"details\": \"Detailed Info about item\", \"clientNotes\": \"any special instructions from client\", \"status\":\"ORDERED\", \"name\":\"Coffee\" } ], \"notes\":\"Note from the customer\", \"discounts\": [ { \"amount\":-200, \"customName\": \"$2 Order Discount\" } ] } }\n")
data = ssl_sock.read()
buffer =""
pp = pprint.PrettyPrinter(indent=4)
while data:
	buffer += data.strip()
	data = ssl_sock.read()

json_result = json.loads(buffer)
pp.pprint(json_result)
ssl_sock.close()
