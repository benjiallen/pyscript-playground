# Lessons learned

## First steps

### Use a basic server

Using the `file:///` protocol seems problematic when trying to load an external python file. It causes a [CORS request not HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors/CORSRequestNotHttp) error.

The solution to this problem seems to be using a basic server to serve the files. Open the terminal and `cd` to the project root. Run `python -m http.server`.
