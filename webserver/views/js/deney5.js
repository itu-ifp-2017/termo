function calculate(){
    var data = {}
    var temperatures = ['10', '20', '30', '40', '50', '60']
    var fields = ['V_1','V_2','V_3','V_4','V_5','P_1','P_2','P_3','P_4','P_5']
    var valid_fields = true;
    $.each(temperatures, function(key,val){
	data[val] = {}
	console.log(val,data[val])
	$.each(fields, function(i,v){
	    var value = $('#'+val+'_'+v).val();
	    data[val][v] = value;
	    if(!value) valid_fields = false;
	});
    });
    console.log(data);
    if(valid_fields){
	$.ajax({
	    url : "/deney5/calculate",
	    type: "POST",
	    data : JSON.stringify(data)
	}).success( function(data, textStatus, jqXHR){
	    if(Object.keys(data).length) window.location = '/deney5/result';
	});
    }
}

$.each(data, function(key,val){
    $.each(val, function(i,v){
	$('#'+key+'_'+i).val(v);
    });
});
