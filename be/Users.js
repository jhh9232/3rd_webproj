const mongoose = require('mongoose')

const userSchema = new mongoose.Schema({
    id:{type:String, required : true, unique : true},
    pw:{type:String, required : true},
    email:{type:String, required: true},
    newcomer:{type:String, required : true}
})

const Users = mongoose.model('3rd_webproj', userSchema)

module.exports=Users
