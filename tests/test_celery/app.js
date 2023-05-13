const {delayQueuedTask} = require("./task")
const celery = require("./celery.config")

celery.init().then( 
    () => {
        console.log("Connected")
        delayQueuedTask("*","*")
    }
)
.catch((err) => { console.log(err)})
