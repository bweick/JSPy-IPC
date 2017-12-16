const net = require('net');

const hostname = '127.0.0.1';
const port = 10000;

var operations = function() {
    this.add = function(x,y) {
        return x+y;
    };

    this.mult = function(x,y) {
        return x*y;
    };
};

const handler = function(socket) {
    socket.on('data', function(bytes) {
        msg = bytes.toString().replace(new RegExp("'", 'g'), "\"");
        msg = JSON.parse(msg);

        var opts =  new operations()
        out = opts[msg.fxn](msg.x,msg.y)
        
        return socket.write(out.toString());
        socket.write('end');
    });
};


const server = net.createServer(handler).listen(port, hostname, () => {
  console.log("Server running at http://"+hostname+":"+port.toString()+"/");
});
