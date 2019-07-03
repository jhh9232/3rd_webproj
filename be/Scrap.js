const mongoose = require('mongoose')

const scrapSchema = new mongoose.Schema({
    user_id:{type:String, required : true},
    Company_title:{type:String, required : true},
    Company_url:{type:String, required : true},
    Recruit_title:{type:String, required : true},
    Recruit_url:{type:String, required : true},
    Careers:{type:String, required : true},
    Position:{type:String, required : true},
    Deadline:{type:String, required : true},
})

const scrap = mongoose.model('scrap', scrapSchema)

module.exports=scrap
