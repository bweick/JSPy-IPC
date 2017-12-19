var TestRPC = require("ethereumjs-testrpc");
var runServer = require("./echo_server")

hostname = process.argv[2];
port = parseInt(process.argv[3]);

console.log(hostname, port)
settings = {
    'port': port,
    'network_id': 50,
    'db_path': './0x_testrpc_snapshot',
    'mnemonic': "concert load couple harbor equip island argue ramp clarify fence smart topic"
}

var server = TestRPC.server(settings);
server.listen(port, hostname, function() {
    console.log("Ethereum node running at http://"+hostname+":"+port.toString()+"/");
    runServer.runServer();
});
