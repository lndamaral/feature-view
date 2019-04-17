#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
import app

def prepare_json_response(success, message, data):
    response = {"meta":{"success":success, "request":request.url}}
    if data:
        response["data"] = data
        response["meta"]["data_count"] = len(data)

    if message:
        response["meta"]["message"] = message

    return response