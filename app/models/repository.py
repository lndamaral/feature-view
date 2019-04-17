#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from git import Repo

class Repository():

    repository = None

    def clone(self, repository_name):
        repository = Repo.clone_from("https://github.com/lndamaral/%s" % repository_name, "temp/%s" % repository_name,  branch='master', recursive=True)

    def clone_branch(self, branch):
        repository = Repo.clone_from("https://github.com/lndamaral/%s" % repository_name, "temp/%s" % repository_name, branch='master', recursive=True)