from sys import argv

from zeep import Client

CLIENT_URL = 'https://www.crcind.com/csp/samples/SOAP.Demo.CLS?WSDL=1'

import requests
import logging
import http.client

http.client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class SoapDemo:
    def __init__(self, client_url=CLIENT_URL):
        client = Client(client_url)
        #client.transport.session.proxies = {
        #    # Utilize for all http/https connections
        #    'http': '127.0.0.1:8080',
        #    'https': '127.0.0.1:8080',
        #}
        self.client = client

    def add_integer(self, a: int, b: int) -> int:
        return self.client.service.AddInteger(a, b)

    def divide_integer(self, a: int, b: int) -> int:
        return self.client.service.DivideInteger(a, b)

    def mission(self) -> str:
        return self.client.service.Mission()

if __name__ == '__main__':
    func = argv[1]
    if not func:
        print('Need to specify func')

    soap_client = SoapDemo()
    if func == 'add':
        res = soap_client.add_integer(argv[2], argv[3])
    elif func == 'div':
        res = soap_client.divide_integer(argv[2], argv[3])
    elif func == 'mission':
        res = soap_client.mission()
        

    print(res)




    
