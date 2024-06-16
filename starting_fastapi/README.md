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

