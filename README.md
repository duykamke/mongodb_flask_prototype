Implemented Flask with MongoDB using Flask-MongoEngine, Flask-PyMongo and Flask-PynamoDB and DDD-driven approach.

The Report Template collection tested with the following "schema" :
```
{
    type: String,
    name: String,
    sub_sections: [
        {
            index: Integer,
            type: String,
            name: String,
            data_type: String,
            sub_sections: [
                ...
            ]
        },
        ...
    ]
}
```

**Running init_mock_mongoengine.py:**

- The runtime for populating 10k records (one by one insertion, not bulk insertion) 
  took 13.46 seconds to complete.

- The runtime for filtering a collection of 10k records (about 25% found in filtered collection) 
  and converting the result to JSON took 0.6 seconds to complete.
  
**Running init_mock_pymongo.py:**

- The runtime for populating 10k records (one by one insertion, not bulk insertion) 
took 8.43 seconds to complete.

- The runtime for filtering a collection of 10k records (about 25% found in filtered collection) 
  and converting the result to JSON took 0.27 seconds to complete.
  
**Running init_mock_pynamodb.py:**

- The runtime for populating only 100 records (one by one insertion, not bulk insertion) 
took 11.6 seconds to complete.

- The runtime for filtering a collection of 100 records (about 25% found in filtered collection) 
  took 5.5e-05 seconds to complete.