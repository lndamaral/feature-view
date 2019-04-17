#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import abort, Blueprint, request, jsonify, g, url_for
from app.utils import *
from app.models.repository import Repository

mod = Blueprint("repositoty", __name__)

@mod.route("/<repository>", methods=["GET"])
def master(repository):
    Repository().clone(repository)

    return jsonify(
        prepare_json_response(
            message=None,
            success=True,
            data={"repository": repository_name}
        )
    )

@mod.route("/<repository>/<string:branch>", methods=["GET"])
def branch(repository, branch):
    Repository().clone_branch(repository_name, "master")
    
    return jsonify(
        prepare_json_response(
            message=None,
            success=True,
            data={"repository": repository, "branch" : branch}
        )
    )