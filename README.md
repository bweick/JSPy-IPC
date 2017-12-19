# JSPy-IPC

Proof of concept for an IPC based Python wrapper to 0x.js library.

Dependencies:
Python:
  <br>socket</br>
  <br>time</br>
  <br>sys</br>
  <br>json</br>
  <br>subprocess</br>
  <br />
JavaScript:
  <br>Node</br>
  <br>0x.js</br>
  <br>Web3</br>
  <br>Ethereumjs-testrpc</br>
  <br>net (Node)</br>

Echo_client.py is the script that sets up both the necessary Ethereum server and JavaScript server in the __init__ function. Since the 
JavaScript server is reliant on the Ethereum server being active in order to have it's Web3 provider set up the js server is only started 
after the Ethereum server is spun up. Once all servers are set up, the Python client can then send queries to the js server through the 
run_process method (which is also used to test if the js server is running before sending meaningful queries) complete with the function 
name to be called and associated variables to run that function. All 0x endpoints are housed within the "operations" object on the js 
server. Once calculations are done on the js server the result is returned back to the Python client. As currently constructed the script 
works using TestRPC as a proof of concept, but expansion to allow for further Web3 providers will be necessary. 
  
  
