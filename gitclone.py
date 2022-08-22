# make sure to install gitpython package and before running this run initgit.sh shell script"

import git
print ("This is gitpython script file")
remoteurl="https://github.com/Akshai183/MyApp.git"
localfloder="/root/gitpython"
myrepo = git.Repo.clone_from(remoteurl, localfloder)
myrepo.git.checkout("master")
