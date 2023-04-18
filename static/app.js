let score = 0
let usedWords = []

$('#main-table').hide()
$('#main-form').hide()
$("#main-form").attr("autocomplete", "off");

$('#start-here').on('submit', function (evt) {

    evt.preventDefault()
    reset()

    let seconds = 4
    let interval = window.setInterval(function () {
	$('#time').text(seconds)
	seconds -= 1
	if (seconds == -1){
	    window.clearInterval(interval)
	    endGame()
	}
    }, 1000)
})

function endGame() {
    
    $('#main-form').hide()
    $('#start-here').show()
    $('#play').show()
    
}

function reset() {

    games()
    score = 0
    usedWords = []
    $('#time').text('')
    $('#result').text('')
    $('#score').text(0)
    $('#word').text('')
    $('#main-table').show()
    $('#main-form').show()
    $('#start-here').hide()
    $('#play').hide()
}


async function games() {

    res = await axios.post('http://127.0.0.1:5000/game_stats', {score : score})
    $('#num_games').text(res.data.num_games)
    $('#high_score').text(res.data.high_score)

}

$('#main-form').on("submit" , async function (evt) {
   
    evt.preventDefault()
    word = retrieveAndResetInputValue()
    if (usedWords.includes(word))
	$('#result').text('Already Used')
    else {
	res = await axios.post('http://127.0.0.1:5000/results', {word : word})
	if (res.data.result == 'ok'){
	    usedWords.push(word)
	    addPointToAndPostScore()
	}
	postSubmissionResult(res, word)
    }
})


function addPointToAndPostScore () {
    score += 1
    postScore()
    return
}

function postScore () {
    $('#score').text(score)
}

function resetScore () {

    score = 0
    return
}

function postSubmissionResult (res, word) {

    $('#word').text(word)
    $('#result').text(res.data.result)
    return
}

function retrieveAndResetInputValue () {

    const word= input.value
    input.value = ''
    return word
}



