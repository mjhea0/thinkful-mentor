$(document).ready(function () {

    $(".reset").click(function() {
        location.reload(true);
    });

    $(".start").click(pythonQuiz);

    function pythonQuiz() {
        var scoreArray = []; // container to hold the score
        var questions = [{
            q: "What is the type of b?<br><code>a = 'bay', b = a[0]</code>",
            s: ["int", "float", "str", "list"],
            a: "str",
            correct: 0
        }, {
            q: "Is this syntax valid?<br><code>a = { i for i in range(0, 10, 2) }</code>",
            s: ["yes", "no"],
            a: "yes",
            correct: 0
        }];

        $(".reset").show()

        var counter = questions.length;

        // append ALL questions to the dom:
        function createQuestion(questions) {
            for (var i = 0; i < counter; i++) {
                $(".start").hide();
                $("#questions").append('<form id="' + i + '"><center><p class="question-num">Question ' +
                    (i + 1) + ' of ' + questions.length + '</p></center><h3 class="question">' +
                    questions[i].q + '</h3><br>' + radioButtons(questions[i].s, i) +
                    '<br><br><button type="submit" class="btn btn-primary next">NEXT QUESTION &#8594;</button></p></form>');
            }
            // hide all questions EXCEPT the first
            for (var k = counter - 1; k > 0; k--) {
                $('#' + k).hide();
            }
        }

        // create radio buttons
        function radioButtons(ary, questionNumber) {
            var answers = [];
            for (i = 0; i < ary.length; i++) {
                answers.push('<div class="radio-inline"><label><input type="radio" name="' +
                    questionNumber + '" value="' + ary[i] + '">' + ary[i] + '</label></div>');
            }
            return answers.join(" ");
        }

        // sums the correct values
        function sumScore(questions) {
            return scoreArray.reduce(function (previousValue, currentValue, index, array) {
                return previousValue + currentValue;
            });
        }

        // checks answer, updates score
        function checkAnswer(answer, questionNumber, questions) {
            if (answer == questions[questionNumber].a) {
                questions[questionNumber].correct = 1;
                scoreArray.push(questions[questionNumber].correct);
            } else {
                scoreArray.push(questions[questionNumber].correct);
            }
        }

        createQuestion(questions);

        $(".next").click(function (event) {
            event.preventDefault();
            var questionNumber = $(this).closest("form").attr("id"); // question number
            var userInput = $('input[name=' + questionNumber + ']:radio:checked').val(); // get answer
            if (counter > 1) {
                // hide current question, show next question
                checkAnswer(userInput, questionNumber, questions);
                $("#" + questionNumber).hide();
                $("#" + questionNumber).next().show();
                counter--;
            } else if (counter === 1) {
                // remove questions, add results
                checkAnswer(userInput, questionNumber, questions);
                $("#questions").find("form").remove();
                $("#questions").append('<h3 class="result"></h3>');
                $(".result").text('You answered ' + sumScore(questions) + ' question(s) correctly out of 10.');
                   for (j = 0; j < scoreArray.length; j++) {
                        if (scoreArray[j] === 0) {
                            console.log(questions[j].q, questions[j].a);
                            $("#questions").append('<p class="missed-' + j + '">You missed:<br> ' +
                                questions[j].q + '<br>Answer: ' + questions[j].a + '</p>');
                        }
                    }
            } else {
                return false;
            }
        });
    }
});
