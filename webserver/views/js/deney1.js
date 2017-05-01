setInterval(function(){
    data = {}
    $('input').each(function(i,v){
	data[i] = v.value;
    });
    $.ajax( {
        url: "/deney1/autosave",
        method: 'POST',
        data: data
    });
}, 5*1000);



function save_exp_data(){
    data = {}
    $('input').each(function(i,v){
	data[i] = v.value;
    });
    $.ajax({
	url : "/deney1/data",
	type: "POST",
	data : data
    }).success( function(msg){
	window.location = msg
    });
}
