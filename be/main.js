var express = require('express')
var app = express()
var router = express.Router()
var fs = require('fs')
var bodyParser = require('body-parser')
var Users = require('./Users')

app.set('views', './')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname +'/public'))

app.listen(3303, function() {
    console.log('Server start')
})

app.get('/',function (req, res) {
    fs.readFile('test.html',function(error,data) {
        if(error) {
            console.log(error)
        }else {
            res.writeHead(200,{'Content-Type':'text/html'})
            res.end(data)
        }
    })
})
app.post('/signup', function(req, res){
    const {Id, Pw, Email, Newcomer}=req.body;
    const u = new Users({id: Id, pw: Pw, email: Email, newcomer: Newcomer})
    u.save().then(r => {
        //res.send({success : true, msg : r})
        res.send('<script>alert("회원가입 성공!"); history.back();</script>');
    }).catch(e => {
        console.log(e)
        res.send({success: false, msg : e.message});
    })
})
app.post('/findone', (req, res, next)=>{
    console.log(req.body.Id)
    Users.findOne({id: req.body.Id}, function(err, obj){
        if(err){
            console.log(err)
            res.send(err)
        }
        console.log(obj)
        res.send('<script>alert("'+obj+'"); history.back();</script>')
    })
})
app.post('/deleteone', (req, res, next)=>{
    console.log(req.body.Id)
    Users.deleteOne({id: req.body.Id}, function(err, obj){
        if(err){
            console.log(err)
            res.send(err)
        }
        console.log(obj)
        res.send('<script>alert("'+obj+'"); history.back();</script>')
    })
})