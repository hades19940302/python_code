
/**
 * @file: demoHelloWorld.js
 * @author: fisco-dev
 * 
 * @date: 2017
 */

var Web3= require('web3');
var config=require('../web3lib/config');
var fs=require('fs');
var execSync =require('child_process').execSync;
var web3sync = require('../web3lib/web3sync');
var BigNumber = require('bignumber.js');


if (typeof web3 !== 'undefined') {
  web3 = new Web3(web3.currentProvider);
} else {
  web3 = new Web3(new Web3.providers.HttpProvider(config.HttpProvider));
}




var filename="HelloEvent";

var express = require('express');
var app = express();
var server = app.listen(3000, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log(' app listening at http://%s:%s', host, port);
});
app.get('/', async function (req, res) {
	var key = req.query.key;
	var address=fs.readFileSync(config.Ouputpath+filename+'.address','utf-8');
	var abi=JSON.parse(fs.readFileSync(config.Ouputpath/*+filename+".sol:"*/+filename+'.abi', 'utf-8'));
	var contract = web3.eth.contract(abi);
	var instance = contract.at(address);
	var addData = instance.addData(key);
	var data_result;
	addData.watch(function(err,result){
		if(!err){
			data_result = result;
			console.log(result);
		}else{
			console.log(err);
		}
	})
	addData.stopWatching();
	var func = "set(string)";
	var params = [key];
	var receipt =  await web3sync.sendRawTransaction(config.account, config.privKey, address, func, params);
	var data = {
		"name":instance.get().toString(),
		"hash":receipt.transactionHash,
		"receipt":receipt,
		"data":data_result,
	}
  	res.json(data);
});

app.get('/get',function(req, res) {
    var hash = req.query.hash;
    data = web3.eth.getTransaction(hash)['input'];
    data_input = hexToAscii(data.slice(138,-1));
    var data_tran_rece = web3.eth.getTransactionReceipt(hash);
    var result;
    function hexToAscii(str1)  
	 {  
	    var hex  = str1.toString();  
	    var str = '';  
	    for (var n = 0; n < hex.length; n += 2) {  
	        str += String.fromCharCode(parseInt(hex.substr(n, 2), 16));  
	    }  
	    return str.replace(/\u0000/g, '');  
	 } ; 
	var version = web3.version.api;
	content = {
		'data':data,
		'data_input':data_input,
		'data_tran_receipt':web3.eth.getTransactionReceipt(hash),
		'data_transaction':web3.eth.getTransaction(hash),
		'version':version,
	} 
    res.json(content);
});






