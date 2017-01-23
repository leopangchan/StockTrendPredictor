var express = require('express');
var path = require('path');
var watson = require('watson-developer-cloud');
var bodyParser = require('body-parser');
var execsync = require('sync-exec');
var fs = require('fs');
var app = express();
var pjson = null;
var dat = "";

var alchemy_language = watson.alchemy_language({
  api_key: '2190f450728492113ce4e5b880a72eefbea73308'
});

// Static paths to be served like index.html and all client side js
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('extra'));
app.use(express.static('nasdaq'));
app.use(bodyParser.json());

app.set('view engine', 'pug');
app.set('views', __dirname+'\\views\\');

app.listen(process.env.NODE_PORT || 3000, process.env.NODE_IP || 'localhost',
function () {
   console.log('App Listening on port 3000');
});

app.post('/', function(req, res) {
	dat = req.body.out;
});

app.get('/post', function(req, res) {
	res.render('post.jade', { message: dat });
});

var waitAlchemy = function(res, params, callback){
  //console.warn("sdfsdf");
  pjson = null;
	alchemy_language.combined(params, function (err, response) {
	   pjson = JSON.stringify(response, null, 2);
	});
	/*console.log(pjson);
	if (pjson == null) {
	 	res.sendStatus(400);
	}*/
	callback();
};

app.get('/subm', function(req, res) {
	var parameters = {
				  extract: 'entities,keywords',
				  sentiment: 1,
				  maxRetrieve: 1,
				  url: "http://finance.ngrok.io/post"
				};
	  waitAlchemy(res, parameters, function(){
      res.send(pjson);
	  	// var jsonp = JSON.parse(pjson);
	  	// //var cname = jsonp.entities[0].name;
	  	// var spawn = execsync('child_process').spawn;
	  	// var proc = spawn('python', ['nasdaq/Nasdaq.py', 'nasdaq/data_dir', cname, "09/13/2016"]);
	  	// proc.kill();
	  	// fs.readFile('nasdaq/output.txt', 'utf8', function(err, data) {
	  	// 	if (err) {
	  	// 		console.log(err);
	  	// 	}
	  	// 	res.send(data);
	  	// });
	 });
});
