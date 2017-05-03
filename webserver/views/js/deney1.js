function trigger_autosave(){
    setInterval(function(){
	autosave_data = {}
	$('input').each(function(i,v){
	    autosave_data[$(v).attr("id")] = v.value;
	});
	$.ajax( {
            url: "/deney1/autosave",
            method: 'POST',
            data: JSON.stringify(autosave_data)
	});
    }, 5*1000);
}

function save_exp_data(){
    data = {}
    $('input').each(function(i,v){
	data[$(v).attr("id")] = v.value;
    });
    $.ajax({
	url : "/deney1/data",
	type: "POST",
	data : JSON.stringify(data)
    }).success( function(msg){
	window.location = msg
    });
}

function fillall(){
    $('input').each(function(i,v){ $('#'+(i+1)).val(parseInt(10*Math.random())); });
}

$.each(data, function(key,val){
    $('#'+key).val(val);
});

if(!Object.keys(data).length){
    $.each(autosave_data, function(key,val){
	$('#'+key).val(val);
    });
    trigger_autosave();
}
