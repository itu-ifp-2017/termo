function save_csv_preview(){
    var validation = check_invalid_column_selections();
    if (validation['status'] == "ok"){
	var id_value = $('#id_dropdown').dropdown('get text');
	var name_value = $('#name_dropdown').dropdown('get text');
	var filename = $('#filename').html();
	var separator = $('#filename').attr('separator');
	$.ajax({
	    url : "/upload/register_from_csv",
	    type: "POST",
	    data : {
		'id_value': id_value,
		'name_value': name_value,
		'filename': filename,
		'separator': separator
	    }
	}).success( function(data, textStatus, jqXHR){
	    window.location = data['redirect_url']
	});
    }else if( validation['status'] == "error" ){
	$('#save_csv_preview').popup({
	    content : validation['msg'],
	    position: 'top center',
	    on: 'manual',
	    hideOnScroll: false
	}).popup('show');
    }
}

function check_invalid_column_selections(){
    var id_value = $('#id_dropdown').dropdown('get value');
    var name_value = $('#name_dropdown').dropdown('get value');
    console.log( id_value, name_value );
    if (id_value == "" && name_value == "") return {"status":"error", "msg": "Please select #ID and Name Columns."}
    else if (id_value == "") return {"status":"error", "msg": "Please select an #ID Column."}
    else if (name_value == "") return {"status":"error", "msg": "Please select a Name Column."}
    else if (id_value == name_value) return {"status":"error", "msg": "#ID and Name Columns can not be same."}
    else return {"status":"ok"}
}
