function calculate(){
    var data = {}
    var gases = ['CO2', 'N2']
    var fields = ['V_1','V_2','V_3','V_4','V_5','V_6','V_7','V_8','V_9','V_10','V_11']
    var valid_fields = true;
    $.each(gases, function(key,val){
	data[val] = {}
	$.each(fields, function(i,v){
	    var value = $('#'+val+'_'+v).val();
	    data[val][v] = value;
	    if(!value) valid_fields = false;
	});
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney7/calculate",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    console.log(data);
	    $.each(data, function(key,val){
		$('#'+key).val(val);
	    });
	});
    }
}
