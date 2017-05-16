function calculate_part_one(){
    var data = {}
    var fields = ['mcal', 'twater', 'mw_mcup', 'teq']
    var valid_fields = true;
    $.each(fields, function(i,v){
	var value = $('#'+v).val();
	data[v] = value;
	if(!value) valid_fields = false;
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney8/calculate_part_one",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    $.each( data, function(k,v){
		$('#'+k).val( v );
	    });
	    console.log(data);
	});
    }
}

function calculate_part_two(){
    var data = {}
    var fields = ['t_1', 't_2', 't_3', 't_4', 't_5', 't_6', 't_7', 't_8', 't_9', 't_10', 'mcold',
		  'dt_1', 'dt_2', 'dt_3', 'dt_4', 'dt_5', 'dt_6', 'dt_7', 'dt_8', 'dt_9', 'dt_10']
    var valid_fields = true;
    $.each(fields, function(i,v){
	var value = $('#'+v).val();
	data[v] = value;
	if(!value) valid_fields = false;
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney8/calculate_part_two",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    window.location = "deney8/result";
	});
    }
}

$.each(data, function(key,val){
    $('#'+key).val(val);
});



// var gases = ['CO2', 'N2']
// var fields = ['V_1','V_2','V_3','V_4','V_5','V_6','V_7','V_8','V_9','V_10','V_11']
// $.each(gases, function(key,val){
//     $.each(fields, function(i,v){
// 	console.log( data, val, v, data[val][v] );
// 	$('#'+val+'_'+v).val( data[val][v] );
//     });
// });
