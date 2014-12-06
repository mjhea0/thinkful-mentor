Here are some toy flask applications that demonstrate individually, various techniques used in web applications.

## FAQ
<i>What is the <b>example-env</b> file I see in some of these repositories?</i>

This might be a hack!  I needed a place to store variables that I didn't want to end up in the git repository, like SECRET_KEY.  What I do is copy example-env to .env, and then add .env to my .gitignore.   I then run 'source .env' to get the environment variables set.

<i>Some of these projects are Heroku projects.  I thought Heroku apps had to be in their own git repository?</i>

See https://github.com/ddollar/heroku-push
