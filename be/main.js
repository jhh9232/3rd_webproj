var express = require('express')
var app = express()
var router = express.Router()
var fs = require('fs')
var bodyParser = require('body-parser')
var Users = require('./Users')
var Scrap = require('./Scrap')
const cors = require('cors'); //cors 설정
var mongoose = require('mongoose');

app.set('views', './')
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname +'/public'))

app.use(cors()) // api 위에서 사용하겠다고 선언


app.listen(3303, function() {
    console.log('Server start')
})

// mongodb setup
mongoose.connect('mongodb://127.0.0.1:27017/3webDB',
 { useNewUrlParser: true }, (err) => {
   if (err) return console.error(err)
   console.log('mongoose connected!')
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
        res.send({success : true, msg : r})
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
        console.log({ success: true, token: obj })
        res.send({ success: true, token: obj })
        //res.send('<script>alert("'+obj+'"); history.back();</script>')
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
        //res.send('<script>alert("'+obj+'"); history.back();</script>')
    })
})
app.post('/scrapCompany', function(req, res){
  const { user_id, company } = req.body
  const s = new Scrap({user_id:user_id,company_title:company.Company_title,
  company_url:company.Company_url,recruit_title:company.Recruit_title,
  recruit_url:company.Recruit_url,careers:company.Careers,position:company.Position,
  deadline:company.Deadline})
  console.log(s)
  s.save().then(r => {
    res.send({success : true})
  }).catch(e => {
    res.send({success : false})
  })
})
app.get('/getScrapCompany/:user_id',function (req, res) {
  const user_id = req.params.user_id
  Scrap.find({user_id:user_id})
  .then(r => {
    res.send({ success: true, msg: r })
  })
  .catch(e => {
    res.send({ success: false, msg: e.message })
  })
})
app.post('/deleteScrapCompany',function (req, res) {
  const { user_id, company_title } = req.body
  Scrap.deleteOne({user_id: user_id,company_title:company_title })
    .then(r => {
      res.send({ success: true, msg: r })
    })
    .catch(e => {
      res.send({ success: false, msg: e.message })
    })
})
