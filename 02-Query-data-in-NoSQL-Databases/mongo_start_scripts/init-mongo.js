salesdb = db.getSiblingDB('catalog')
// salesapidb.createCollection("debug"); //MongoDB creates the database when you first store data in that database
// salesapidb.debug.insert({"message": "Init DB"})

db.createUser(
    {
        user: "bert",
        pwd: "bertpassword",
        roles: [
            {
                role: "readWrite",
                db: "sales"
            }
        ]
    }
);