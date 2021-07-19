
git add .
git commit -m "put your comment here"

git push origin

git tag -a $(git describe) -m "Some another comment"
git push origin --tags
