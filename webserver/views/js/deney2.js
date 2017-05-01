$('#m1').focusout(function(){
    if($(this).val() && $('#mcup').val()){
	$('#mcold').css("text-align","right")
	    .css("padding-right","10px")
	    .val( ($(this).val() - $('#mcup').val()).toFixed(2) );
    }else{
	$('#mcold').val('');
    }
});

function calculate_part_one(){
    var data = {}
    var fields = ['mcup', 'm1', 'T1', 'T2', 'Teq', 'm2']
    var valid_fields = true;
    $.each(fields, function(i,v){
	var val = $('#'+v).val();
	data[v] = val;
	if(!val) valid_fields = false;
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney2/calculate_part_one",
	    type: "POST",
	    data : data
	}).success( function(data, textStatus, jqXHR){
	    $.each(data, function(key,val){
		$('#'+key).val(val);
	    });
	});
    }
}

function calculate_part_two(){
    var data = {}
    var materials = ['glass', 'iron', 'graphite']
    var fields = ['m_water', 'T2', 'M', 'T1', 'Tf'];
    var valid_fields = true;
    $.each(materials, function(ind,val){
	data[val] = {}
	$.each(fields, function(i,e){
	    var value = $('#'+val+'_'+e).val();
	    data[val][e] = value;
	    if(!value) valid_fields = false;
	});
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney2/calculate_part_two",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    $.each(data, function(key,val){
		$('#'+key).val(val);
	    });
	});
    }
}
