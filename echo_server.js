const ZeroEx = require('0x.js');
const Web3 = require('web3');

const net = require('net');

// const hostname = process.argv[2];
// const port = parseInt(process.argv[3]);

const hostname = 'localhost';
const port = 10000;

const provider = new Web3.providers.HttpProvider('http://localhost:8545');
const zeroEx = new ZeroEx.ZeroEx(provider);

var operations = function() {

    this.salt = function(vars) {
        return ZeroEx.ZeroEx.generatePseudoRandomSalt();
    };

    this.zrxAddress = async function(vars) {
        try {
            return await zeroEx.exchange.getZRXTokenAddressAsync();
        } catch (err) {
            console.log(err);
        }
    };

    this.testConnection = async function() {
      return true
    }

    this.nullAddress = function(vars) {
        return ZeroEx.ZeroEx.NULL_ADDRESS;
    }
};

const handler = function(socket) {
    socket.on('data', async function(bytes) {
        msg = bytes.toString().replace(new RegExp("'", 'g'), "\"");
        msg = JSON.parse(msg);

        var opts =  new operations()
        out = await opts[msg.fxn](msg.vars)

        return socket.write(out.toString());
        socket.write('end');
    });
};

const runServer = () => net.createServer(handler).listen(port, hostname, () => {
  console.log("Server running at http://"+hostname+":"+port.toString()+"/");
});

module.exports.runServer = runServer
