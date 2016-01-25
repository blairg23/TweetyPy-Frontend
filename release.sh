git add --all
git commit -m "$1"
git push && git push --mirror https://blairg23@bitbucket.org/blairg23/tweetypy-frontend.git
git status