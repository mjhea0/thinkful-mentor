wtf_quiz
========
This is a small example of how I am using WTforms, Jinja2 and Flask to create a quiz.

The validator EqualTo didn't do exactly quite what I wanted to do. It could
be because I wasn't sure what I was doing...
But anyway, I decided to create my own custom validator which I called CorrectAnswer.
The CustomValidator also has an added function that gives a random error message.

The form is validated when the answer given to the form matches what you give to CorrectAnswer.

Once validated, it takes you to another page. In this example, it's just a "Congratulations" page.  

Also, on the HTML page for the quiz (wtf_quiz.html), I added an IF statement to check if it is the
first or last iteration of the FOR loop. If the IF statement is TRUE, then 'question.label'
will not be printed. 
The first iteration prints the Csrf_Token label and the last iteration prints the "Submit" label. 
This added IF statement prevents that from printing. 

