#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gherkin.token_scanner import TokenScanner
from gherkin.parser import Parser
from flask import request

import glob
import app
import os

def prepare_json_response(success, message, data):
    
    response = {"meta":{"success":success, "request":request.url}}
    
    if data:
        response["data"] = data
        response["meta"]["data_count"] = len(data)

    if message:
        response["meta"]["message"] = message

    return response

def findFeaturesDir(repository):
    for root, dirs, files in os.walk("temp/%s" % repository, topdown=False):
        for name in dirs:
            if (name == "features"):
                return os.path.join(os.path.abspath(root), name)


def findFeaturesFiles(path):
    os.chdir(path)
    return glob.glob("*.feature", recursive=True)

def parseFeatureFile(path, files):
    parser = Parser()
    feature = parser.parse(TokenScanner(path + "/" + files))
    return feature

def getAllFeatureNames(path, files):
    menu = []
    for feature_file in files:
        menu.append(parseFeatureFile(path, feature_file)['feature']['name'])
    return menu

def parseAllFeatureFiles(path, files):
    feature_list = []
    for feature_file in files:
        feature_list.append(parseFeatureFile(path, feature_file))
    return feature_list