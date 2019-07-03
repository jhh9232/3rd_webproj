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
// User.updateOne({ _id: '5cbd50967c00ec110c8d7912' }, { $set: { age: 27 } })
app.put('/update', (req, res, next)=>{
    console.log(req.body)
    Users.updateOne({ id: req.body.id }, { $set: { email: req.body.email ,newcomer:req.body.newcomer} })
    .then(r => {
      res.send({success : true})
    }).catch(e => {
      res.send({success : false, msg: e.message})
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
  const s = new Scrap({user_id:user_id,Company_title:company.Company_title,
  Company_url:company.Company_url,Recruit_title:company.Recruit_title,
  Recruit_url:company.Recruit_url,Careers:company.Careers,Position:company.Position,
  Deadline:company.Deadline})
  console.log(s)
  s.save()
  .then(r => {
    res.send({success : true})
  }).catch(e => {
    res.send({success : false, msg: e.message})
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
  Scrap.deleteOne({user_id: user_id,Company_title:company_title })
    .then(r => {
      res.send({ success: true, msg: r })
    })
    .catch(e => {
      res.send({ success: false, msg: e.message })
    })
})
