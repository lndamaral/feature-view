#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import app
from git import Repo

class Repository():

    def clone(self, repository):
        Repo.clone_from("git@github.com:ihm-software/%s.git" % repository, "temp/%s" % repository, branch='master')

    def clone_branch(self, repository, branch):
        repo = None
        if (os.path.exists("temp/%s" % repository)):
            repo = Repo("temp/%s" % repository)
        else:
            repo = Repo.clone_from("git@github.com:ihm-software/%s.git" % repository, "temp/%s" % repository)
                               
        git_ = repo.git
        git_.checkout(branch)
        git_.pull("--rebase")