# node-graphql
> Student management system backend GraphQL server.

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed the `node-graphQl` app run on Windows, you should have little problem getting
up and running.


## Setup
- NPM stable version
- Node stable version
- Docker (If you want ot run the project docker container)

```bash
git clone https://github.com/mbrsagor/nodeGraphql.git
cd nodeGraphql
npm install
npm start
```

###### GraphQL query example:
```javascript
query ExampleQuery {
  enrollment {
    id
    email
    fullName
    dept
  }
}
```
Response body:
```javascript
{
  "data": {
    "enrollment": [
      {
        "id": "1",
        "email": "ada@telixia.com",
        "fullName": "Ada Eze",
        "dept": "Software Engineering"
      },
      {
        "id": "2",
        "email": "musa@telixia.com",
        "fullName": "Musa Bashir",
        "dept": "Data Engineering"
      }
    ]
  }
}
```

###### Operation example:
```javascript
mutation {
  registerStudent(
    email: "ohi@sagor.me",
    fullName: "Sagor",
    ) {
    id
    email
    fullName
    dept
    enrolled
  }
}
```
Response body:
```javascript
{
  "data": {
    "registerStudent": {
      "id": "6",
      "email": "contact@telixia.com",
      "fullName": "Sammy",
      "dept": null,
      "enrolled": false
    }
  }
}
```
