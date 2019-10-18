#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import app
from git import Repo

class Repository():

    def clone_branch(self, repository, branch):

        repo = None

        if (os.path.exists("temp/%s" % repository)):
            repo = Repo("temp/%s" % repository)
        else:
            repo = Repo.clone_from( "https://github.com/{0}/{1}.git".format(os.getenv('GITHUB_PROFILE'), repository), 
                                    "temp/%s" % repository)
                               
        git_ = repo.git
        git_.checkout(branch)
        git_.pull("--rebase")