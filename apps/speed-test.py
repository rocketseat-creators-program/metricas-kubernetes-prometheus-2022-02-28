import speedtest
import time
import os
from prometheus_client import start_http_server, Gauge

servers = []
testReady = 0
test_interval = 120 # seconds
datahora = time.time()
agora = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
download_speed = Gauge('speedtest_download', 'Download speed')
upload_speed = Gauge('speedtest_upload', 'Upload speed')
ping_latency = Gauge('speedtest_ping', 'Ping Latency')

debug = os.getenv('SPEED_DEBUG')
outPort = os.getenv('SPEED_PORT')
if debug in [None, False, "", "0", 0]: debug = 0
else: debug = 1
if outPort and outPort.isnumeric():  outPort = int(outPort)
else: outPort = 9095
print(f"{agora} [INFO] - debug: {debug}, Port: {outPort}, Test Interval: {test_interval}")

# Setup da biblioteca
try: s = speedtest.Speedtest()
except Exception as err:
  testReady = 0
  print(f"{agora} [ERROR] - creating speedtest s: {err}")
else:
  testReady = 1
  print(f"{agora} [INFO] - Success creating speedtest s: {testReady}")
# Prepara dados para o Prometheus
def process_request(interval):
  if testReady:
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    results_dict = s.results.dict()
    download_speed.set(results_dict["download"])
    upload_speed.set(results_dict["upload"])
    ping_latency.set(results_dict["ping"])
    print(f"{agora} [INFO] - upload: {results_dict['upload']}, download: {results_dict['download']}, ping: {results_dict['ping']}")
  else: print(f"{agora} [ERROR] - Test not ready: {testReady}")
  time.sleep(interval)
  
if __name__ == '__main__':
  # Start up the server to expose the metrics.
  start_http_server(outPort) 
  while True:
    try:
      process_request(test_interval)
    except Exception as err:
      print(f"{agora} [ERROR] - request error in main: {err}")
      time.sleep(test_interval)
