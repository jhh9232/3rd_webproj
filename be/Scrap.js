const mongoose = require('mongoose')

const scrapSchema = new mongoose.Schema({
    user_id:{type:String, required : true},
    company_title:{type:String, required : true},
    company_url:{type:String, required : true},
    recruit_title:{type:String, required : true},
    recruit_url:{type:String, required : true, unique: true},
    careers:{type:String, required : true},
    position:{type:String, required : true},
    deadline:{type:String, required : true},
})

const scrap = mongoose.model('scrap', scrapSchema)

module.exports=scrap
