# Why We Need Schema:
- Its a pain to get all the values from body.
- The client can send whatever data they want.
- The data isn't getting validated.
- We need to validate the data before processing it.
- We ultimately force the client to send data in a schema that we expect.

## Using Pydantic for Schema Creation
- Pydantic is a Python library that allows you to create robust, strongly typed models with runtime
validation. It's perfect for creating robust APIs.
- It's used to define the structure of the data that we expect to receive from the client.
- It's used to validate the data that we receive from the client.
- It's used to convert the data into Python objects that we can easily work with.
- It's used to generate documentation for our API.

### Pydantic Field Types 
`Which we have used in Class`
- `str`: String
- `int`: Integer
- `float`: Floating Point Number
- `bool`: Boolean
- `list`: List of items
- `dict`: Dictionary
- `datetime`: Date and Time
- `Optional`: Makes a field optional
- `Union`: Allows a field to be one of multiple types
- `List[Item]`: A list of items of type Item
- `Dict[str, Item]`: A dictionary with string keys and values of type Item
- `Literal["value1", "value2", ...]`: A string that must be one
of the specified values
- `HttpUrl`: A URL
- `EmailStr`: An email address
- `IPvAnyAddress`: An IP address
- `IPv4Address`: An IPv4 address
- `IPv6Address`: An IPv6 address


For More check this [link.](https://docs.pydantic.dev/1.10/usage/types/)

#### CRUD 
![CRUD](data:image/png;base64,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)



## API Endpoints

This table summarizes the available API endpoints for managing posts:

| Action | Description | Endpoint | Method |
|---|---|---|---|
| Create | Create a new post | `/posts` | POST |
| Read (All) | Get all posts | `/posts` | GET |
| Read (Specific) | Get a specific post by ID | `/posts/{id}` | GET |
| Update | Update an existing post | `/posts/{id}` | PUT/PATCH |
| Delete | Delete a post | `/posts/{id}` | DELETE |

**Note:**

- Replace `{id}` in the endpoints with the actual ID of the post you want to access or update.

**Additional Considerations:**

- You can add a brief explanation of the request body format for POST and PUT requests if applicable.
- Mention any authentication or authorization requirements for accessing these endpoints.


## What is a DataBase

- Database is a collection of organized data that can be easily accessed and managed.
- We don't work or interact with Databse directly.
- Instead we make use of a Software reffered to as a Database Management Software ( **DBMS** )

## Types of DataBases

| Relational | NoSQL |
|------------|-------|
| MYSQL | MongoDB|
| POSTGRESQL | DynamoDB |
| ORACLE | ORACLE |
| SQL SERVER | SQL SERVER |


We will use **Relational Databases** in this project most specifically **POSTGRESQL**.

But remember other relational databases are 90% same to **POSTGRESQL**.

## Relational Database & SQL 
- Structured Query Language ( **SQL** ) - Language used to communicate with **DBMS**.


![SQL](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnKepQgurfYPGLG9VniAgxtJsCk-JiPvKbxVauf80GT1b0D9W-Deu_Wd1kMcfJPNSndRs&usqp=CAU)
 
## POSTGRES
- Each instance of postgres can be carved into multiple separate databases.

![POSTGRESQL](https://docs.aws.amazon.com/images/prescriptive-guidance/latest/saas-multitenant-managed-postgresql/images/saas-postgresql-bridge-dbs.png)

- By default every Postgres installation comes with one database already created called **"postgres"**
- This is important because postgres requires you to specify the name of a database to make a connection. So there needs to always be one database.

## Tables
- A table represents a subject or event in an application.

![Tables](https://blog.airtable.com/content/images/2020/12/Database-_-Tables.png)


### Coloumns & Rows 

- A table is made up of coloumns and rows.
- Each coloumn represents a differnet attribute.
- Each row represent a different entry in the table.


![Coloumns_and_rows](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdcKLqA194mvFbWi7tt-dmqVKulVtX0NEpdQ&s)


### Postgres DataTypes

- Database have datatypes just like any other programming language.

![Postgres_DataTypes](https://static.javatpoint.com/postgre/images/postgresql-data-types.png)


#### Primary Key

- Is a coloumn or group of coloumns that uniquely identifies each row in a table.
- Table can have one and only one **primary key**.


![primary_key](data:image/png;base64,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)

- The Primary key does not have to be the ID coloumn always. It's upto you to decide which coloumn uniquely defines each record.


### Null Constraints
- By default, when adding a new entry to database, any coloumn can be left blank. When a coloumn is left blank, it has a **NULL** value.

- If you need coloumn to properly filled in to create a new record, a **NOT NULL** constraint can be added to the coloumn to ensure that the coloumn is never left blank. 





### Psycopg - PostgreSQL database  adopter for python:
- When comes to postgres to use it in a python project we need a postgres driver.
- We will be using `Psycopg`

## `ORM (Object Relational Mapper)`

- Layer of Abstraction that sits between the database and us.
- We can perform all database operations through python code. **No More SQL.**

![ORM](https://qph.cf2.quoracdn.net/main-qimg-13b582c595a67086b86d7691f88d80bd)


#### What ORM's can do
- Instead of manually defining tables in postgres, We can define our tables as python models.
- Queries can be made excusively through python code. **No SQL is neccessary.**

## `SQLALCHEMY`
- `SQLALCHEMY` is one the most popular python ORM.
- It is a standalone library and has no association with FastAPI. It can be used with anyother python web framework or any python based application.
- `pip install sqlalchemy`


## `SCHEMA MODELS`
- Schema / Pydantic defines the structure of a request and response.
- This ensures when a user wants to create a post, the request will only go through if it has a **`title`** and **`content`** in the body. 

## `SQLALCHEMY MODELS`
- SQLALCHEMY models define the structure of a table in the database.
- This ensures when a user wants to create a post, the post will only be created if it
has a **`title`** and **`content`** in the database.
- Responsible for defining the coloumns of our `"posts"` tables within the postgres.
- sqlalchemy is used to query , create , delete and update entries within the database.


#### Bcrypt
- We will be using Bcrypt for hashing passwords
- `pip install bcrypt`
- Bcrypt is a password hashing function designed by Niels Provos and David Mazières,
based on the Blowfish cipher. The hash value produced by bcrypt is designed to be slow and comput
ionally expensive, making it suitable for hashing passwords.
- Bcrypt is a one-way function, meaning it's easy to generate a hash from a password
but it's very hard to generate a password from a hash.


##### utils.py file
- it stores functions 
- utility functions 
- functions that are used across multiple files
- functions that are not specific to any particular file or class
- functions that are used to perform some common tasks
- functions that are used to perform some utility tasks

###### Prefix
- Prefix is used to define the route prefix for all routes in the router.
- For example, if you have a router with a prefix of "/api/v1", all routes
defined in that router will have "/api/v1" prepended to their path.
- Prefix is used to group related routes together.
- Prefix is used to version APIs.
- - Prefix is used here in post.py and user.py so we can't write /post/ but instead we write it like / . check the code with previous commits.

###### Tags
- Tags are used to group related routes together.
- Tags are used to categorize routes.
- Tags are used to generate documentation for APIs.
- Tags are used to generate OpenAPI documentation for APIs.
- Tags are used here in post.py and user.py so we can't write /post/ but
instead we write it like / . check the code with previous commits.


## JWT token Authentication

![jwt](https://documentation.softwareag.com/webmethods/compendiums/v10-5/C_API_Management/api-mgmt-comp/images/workflow_jwt.png)

JWT (JSON Web Token) is a popular stateless authentication method for APIs and web applications. It works by creating a token containing encoded user information that is sent between the client and server. This token allows the server to verify the user's identity without needing to store session data on the server itself. JWT offers advantages like scalability and flexibility, making it suitable for microservices architectures and cross-origin requests. However, it requires careful implementation to ensure security, as stolen tokens can grant access to user accounts.
Here's how JWT token authentication works:
1. **User registration**: The user registers with the application, providing credentials like username and password.
2. **Login**: The user logs in with their credentials, and the server verifies them.
3. **Token generation**: If the credentials are valid, the server generates a JWT token containing the
user's ID, username, and other relevant information. This token is signed with a secret key to
prevent tampering.
4. **Token transmission**: The server sends the JWT token to the client, usually in the HTTP
response header or as a cookie.
5. **Token verification**: On subsequent requests, the client sends the JWT token back to the
server. The server verifies the token by checking its signature and ensuring it hasn't expired.
6. **Access granted**: If the token is valid, the server grants access to the requested resources
or performs the requested actions.
7. **Token refresh**: When the token expires, the client can request a new token using the
refresh token, which is usually sent along with the initial token.
Here are some benefits of using JWT token authentication:
* **Stateless**: JWT tokens don't require server-side session storage, making them scalable and
efficient.
* **Flexible**: JWT tokens can be used across multiple domains and services, making them suitable
for microservices architectures.
* **Secure**: JWT tokens are digitally signed, making them tamper-proof and secure.
* **Easy to implement**: JWT token authentication is relatively easy to implement, especially
when compared to other authentication methods like OAuth.
However, JWT token authentication also has some limitations and potential security risks, such as:
* **Token theft**: If an attacker steals a JWT token, they can use it to gain unauthorized
access to the application.
* **Token expiration**: If tokens are not properly configured to expire, they can remain valid
indefinitely, allowing attackers to use them.
* **Key management**: The secret key used to sign JWT tokens must be kept secure and
managed properly to prevent unauthorized access.

**In Short:**
- JWT Authentication is stateless.
- JWT Authentication is scalable.
- JWT Authentication is secure.
- JWT Authentication is fast.
- JWT Authentication is widely used.
- JWT Authentication is used to authenticate users.
- JWT Authentication is used to authorize users.
- JWT token is generated when user logs in.
- JWT token is sent in the header of every request.

#### Purpose of Signature in JWT
- The signature in JWT serves several purposes:
    1. **Authentication**: The signature ensures that the token was issued by the expected party (
    e.g., the server) and not tampered with during transmission.
    2. **Integrity**: The signature guarantees that the token's contents have not been altered or
    tampered with.
    3. **Non-repudiation**: The signature provides proof that the token was issued
    by the server, making it difficult for the server to deny having issued the token.
    4. **Verification**: The signature allows the server to verify the authenticity of the token
    and ensure it has not been tampered with or altered.
    5. **Security**: The signature adds an extra layer of security to the token, making
    it more difficult for attackers to create or modify tokens.
    6. **Trust**: The signature establishes trust between the client and server, ensuring that
    the token is genuine and has not been tampered with.
    7. **Validation**: The signature enables the server to validate the token and ensure it
    meets the expected format and structure.
    8. **Protection**: The signature protects the token from unauthorized access, tampering,
    and manipulation.


##### FORIEGN KEY

how  any coloumn is conneted to any table.

#### Query Parameters
- Query parameters are a way to pass additional data from the client to the server as part of the URL
- They are used to filter, sort, or paginate data, or to specify additional options for the
request.
- Query parameters are appended to the URL using a question mark (?) and are separated by
ampersands (&).
- Query parameters are not part of the URL's path, but rather are appended to the URL's
query string.
- Query parameters are usually used for filtering, sorting, or paginating data, or for
specifying additional options for the request.

https://www.youtube.com/watch?v=0sOvCWFmrtA

Here `?v=0sOvCWFmrtA` is the query parameter.