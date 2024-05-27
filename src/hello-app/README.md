
# hello-app
This is a simple hello-world Python flask web app.

## Download and Install
Get the latest release from (here)[]. Download either the `*.tar.gz` or the `*.whl` package.
Install using pip, for example:
```shell
$ python3 -m pip install hello_app-0.1.tar.gz
```
or
```shell
$ python3 -m pip install hello_app-0.1-py3-none-any.whl
```

## usage
Start the server with the default config:

```shell
$ hello-app run
```
or with custom IP/port
```shell
$ hello-app run --port 8080
```
see `hello-app run -h` for details

Head to the browser or use `curl` to say hello
```shell
$ curl -X GET http://127.0.0.1:5000/hello/
Hello there!

# or
p$ curl -X GET http://127.0.0.1:5000/hello-json/
{
  "message": "Hello there!"
}
```
or say hello to someone
```shell
$ curl -X GET http://127.0.0.1:5000/hello/Abeer
Hello Abeer!

#or
$ curl -X GET http://127.0.0.1:5000/hello-json/AbeerM
{
  "message": "Hello AbeerM!"
}
```
It's as simple as that!

## Notes
- Developed and tested using Python 3.10, other versions haven't been tested.