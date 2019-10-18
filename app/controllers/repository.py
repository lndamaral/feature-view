#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, Blueprint, request, jsonify, g, url_for, render_template
from app.utils import *
from app.models.repository import Repository

mod = Blueprint("repository", __name__)

@mod.route("/<repository>", methods=["GET"])
def master(repository):

    Repository().clone_branch(repository, "master")

    path = findFeaturesDir(repository)
    files = findFeaturesFiles(path)
    menu = getAllFeatureNames(path, files)
    features = parseAllFeatureFiles(path, files)[0]

    print(prepare_json_response(
        message=None,
        success=True,
        data={"repository": repository, "branch" : "master"}
    ))

    return render_template('index.html', features=features, menu=menu, repository=repository)

@mod.route("/<repository>/feature/<string:feature>", methods=["GET"])
def feature(repository, feature):

    Repository().clone_branch(repository, "master")

    path = findFeaturesDir(repository)
    files = findFeaturesFiles(path)
    menu = getAllFeatureNames(path, files)
    features = parseAllFeatureFiles(path, files)

    for f in features:
        if f['feature']['name'] == feature:
             return render_template('index.html', features=f, menu=menu, repository=repository)
    
    return render_template('index.html', features=features[0], menu=menu, repository=repository)

    print(prepare_json_response(
        message=None,
        success=True,
        data={"repository": repository, "branch" : "master"}
    ))

    return render_template('index.html', features=features, menu=menu)


@mod.route("/<repository>/<string:branch>", methods=["GET"])
def branch(repository, branch):

    Repository().clone_branch(repository, branch)
    
    features_dir = findFeaturesDir()

    return jsonify(
        prepare_json_response(
            message=None,
            success=True,
            data={"repository": repository, "branch" : branch}
        )
    )