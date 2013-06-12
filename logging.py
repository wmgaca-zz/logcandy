#!/usr/bin/env python
# coding=utf-8

# TODO(wmgaca): set up logging
__logger = None

_INDENT = ''
_INDENT_STEP = 4


def __log(logger_function, message):
    logger_function(_INDENT + str(message))
    return __logger


def indent():
    global _INDENT
    _INDENT += ' ' * _INDENT_STEP
    return __logger


def unindent():
    global _INDENT
    if len(_INDENT) >= _INDENT_STEP:
        _INDENT = _INDENT[:-_INDENT_STEP]
    return __logger


def get_indent_size():
    return len(_INDENT)


def info(message):
    return __log(__logger.info, message)


def debug(message):
    return __log(__logger.debug, message)


def warning(message):
    return __log(__logger.warning, message)


def error(message):
    return __log(__logger.error, message)


def blank():
    return __log(__logger.info, '')
