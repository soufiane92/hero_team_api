import logging
import sys
import json


class SplunkFormatter(logging.Formatter):
    """Class to define the log format that will be compatible with Splunk"""
    def format(self, record):
        log_data = {
            "level": record.levelno,
            "logger_name": record.name,
            "python_module": record.module,
            "filename": record.filename,
            "line_number": record.lineno,
            "time": int(record.created),
            "msg": record.getMessage(),
            "pid": record.process,
        }
        if "process_uuid" in record.__dict__:
            log_data["process_uuid"] = record.__dict__["process_uuid"]

        return json.dumps(log_data)


class SplunkUvicornFormatter(logging.Formatter):
    """Class to define the log format that will be compatible with Splunk"""
    def format(self, record):
        log_data = {
            "level": record.levelno,
            "logger_name": record.name,
            "time": int(record.created),
            "msg": record.getMessage(),
            "pid": record.process,
        }
        if "method" in record.__dict__:
            log_data["method"] = record.__dict__["method"]
        if "url" in record.__dict__:
            log_data["url"] = record.__dict__["url"]
        if "status_code" in record.__dict__:
            log_data["status_code"] = record.__dict__["status_code"]
        if "client_ip" in record.__dict__:
            log_data["client_ip"] = record.__dict__["client_ip"]

        return json.dumps(log_data)


def get_logger(logger_name=None):
    logger_name = logger_name or __name__
    if logging.getLogger(logger_name).hasHandlers():
        custom_logger = logging.getLogger(logger_name)
    else:
        custom_logger = logging.getLogger(logger_name)
        if logger_name == "uvicorn":
            logging_formatter = SplunkUvicornFormatter()
            logging.getLogger("uvicorn.access").disabled = True
        else:
            logging_formatter = SplunkFormatter()
        custom_logger.propagate = False
        custom_logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(logging_formatter)
        console_handler.setLevel(logging.DEBUG)
        custom_logger.addHandler(console_handler)

    return custom_logger