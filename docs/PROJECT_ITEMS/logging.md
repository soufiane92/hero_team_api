## Logging
### General overview
Logs are generated across the entire application.
They are sent to `stdout` and `stderr` by the python logger package.
Logs are in a json format to facilitate the log recognition and manipulation later on.

### Python
A logger class is present in `app/utils`.
In order to use a logger, the dev need to call the `get_code_logger` method and to define a logger name.
Then he can just call it