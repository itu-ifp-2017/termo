$('#mw_mcup').focusout(function(){
    if($(this).val() && $('#mcup').val()){
	$('#mcold').css("text-align","right")
	    .css("padding-right","10px")
	    .val( $(this).val() - $('#mcup').val() );
    }else{
	$('#mcold').val('');
    }
});
