const URL = 'http://localhost:5001'

var button = document.getElementById('inp_btn')

var inputs = [['LichessUsername', 'lichessuser'], ['ChesscomUsername', 'chesscomuser']]

button.onclick = function(){
    
    data = {} 

    for (i = 0; i < inputs.length; i++){

        data[inputs[i][0]] = document.getElementById(inputs[i][1]).value

    }

    $.post(URL, data, function(data, status){
        console.log('Responded with: ', status)
        if (status == 'success') {
            close();
        }
    })
    console.log(data)
}