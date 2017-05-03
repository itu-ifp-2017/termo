function calculate(){
    var data = {}
    var fields = ['m1', 'm2', 'T1', 'm3', 'T2']
    var valid_fields = true;
    $.each(fields, function(i,v){
	var val = $('#'+v).val();
	data[v] = val;
	if(!val) valid_fields = false;
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney3/calculate",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    $.each(data, function(key,val){
		$('#'+key).val(val);
	    });
	});
    }
}

$.each(data, function(key,val){
    $('#'+key).val(val);
});
