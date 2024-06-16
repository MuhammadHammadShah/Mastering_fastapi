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
