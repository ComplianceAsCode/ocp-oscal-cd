#!/bin/bash

export COMMIT_TITLE="chore: Component definitions automatic update."
export COMMIT_BODY="Sync components with OCP4-cd repo"
git clone https://$GITHUB_TOKEN@github.ibm.com/compliance-trestle-testing/ocp4-ssp
cd ocp4-ssp
git checkout -b "cd_autoupdate_$TRAVIS_BUILD_NUMBER"
cp -r ../component-definitions .
if [ -z "$(git status --porcelain)" ]; then 
  echo "Nothing to commit" 
else 
  git diff
  git add component-definitions 
  git commit -m "$COMMIT_TITLE"
  git push -u origin "cd_autoupdate_$TRAVIS_BUILD_NUMBER"
  echo $COMMIT_BODY
  curl -u Ekaterina-Nikonova:$GITHUB_TOKEN -X POST -H "Accept: application/vnd.github.v3+json"  https://api.github.ibm.com/repos/compliance-trestle-testing/ocp4-ssp/pulls -d '{"head":"'"cd_autoupdate_$TRAVIS_BUILD_NUMBER"'","base":"develop","body":"'"$COMMIT_BODY"'","title":"'"$COMMIT_TITLE"'"}'

fi

