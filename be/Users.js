const mongoose = require('mongoose')
mongoose.connect('mongodb://127.0.0.1:27017/3webDB')
var db = mongoose.connection;
db.on('error', function(){
    console.log("Connection Failed")
})
db.once('open', function(){
    console.log("Connect")
})
const userSchema = new mongoose.Schema({
    id:{type:String, required : true, unique : true},
    pw:{type:String, required : true},
    email:{type:String, required: true},
    newcomer:{type:String, required : true}
})

const Users = mongoose.model('3rd_webproj', userSchema)

module.exports=Users