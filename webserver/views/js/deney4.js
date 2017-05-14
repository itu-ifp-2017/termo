function calculate(){
    var data = {}
    var fields = ['L1', 'T1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8']
    var valid_fields = true;
    $.each(fields, function(i,v){
	var val = $('#'+v).val();
	data[v] = val;
	if(!val) valid_fields = false;
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney4/calculate",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    console.log(data);
	    $.each(data, function(key,val){
		if(key == 'fig'){
		    $('#fig').attr("src", "/static/"+val).css("visibility", "visible");
		}else{
		    $('#'+key).val(val);
		}
	    });
	});
    }
}

$.each(data, function(key,val){
    if(key == 'fig'){
	$('#fig').attr("src", "/static/"+val).css("visibility", "visible");
    }else{
	$('#'+key).val(val);
    }
});
