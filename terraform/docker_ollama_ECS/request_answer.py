import requests
query="http://ollama-alb-1022310736.us-east-1.elb.amazonaws.com/generate?prompt=describe+major+principles+of+prompt"
print(query)
result= requests.get(query).json()
print('model =', result['model'])
print(result['output'])