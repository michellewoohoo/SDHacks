const http = require('http');
const fs = require('fs');
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer(function(req, res){
	console.log('request was made: ' + req.url);
	if(req.url === '/home' || req.url === '/'){
		res.writeHead(200, {'Content-Type': 'text/html'});
		fs.createReadStream(__dirname + 'home.html').pipe(res);
	}
});

server.listen(port, hostname);
console.log(`Server running at http://${hostname}:${port}/`);