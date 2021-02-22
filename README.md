Implemented Flask with MongoDB using Flask-MongoEngine and DDD-driven approach.

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

**Running init_mock_database.py:**

- The runtime for populating 1k records (one by one insertion, not bulk insertion) 
took 2.4 seconds to complete.

- The runtime for filtering roughly 25% of 1k records took 0.04 seconds to complete.
