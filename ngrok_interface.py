from pyngrok import ngrok
# import time

ngrok_tunnel = ngrok.connect(22, 'tcp')

with open('/ngrok_process', 'w') as file:
    file.write(ngrok_tunnel.public_url)


ngrok_process = ngrok.get_ngrok_process()

try:
    # Block until CTRL-C or some other terminating event
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down server.")

    ngrok.kill()

