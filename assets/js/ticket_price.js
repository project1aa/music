
function calculate_price(type)
{
	$('#id_row').on('change', function() {
			var row = this.value;
			
			$.ajax({
	    	url: '/calculate_price/',
	    	data: {
	      	'row': row,
	      	'type': type
	    },
	    
	    dataType: 'json',
	    
	    success: function (data) {
	      if (data) {
	        $("#price").text(data.price);
	      }
	    }
	  });

	})
}
