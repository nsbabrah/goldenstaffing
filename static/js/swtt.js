 
 $(document).ready(function() {
$("#btnShowAlert").click(function() {
 	swal("you info is submit")
 	 type: "warning",   
 	 confirmButtonColor: "#DD6B55",   
 	 confirmButtonText: "Yes, delete it!",   
 	 cancelButtonText: "No, cancel plx!",   
 	 closeOnConfirm: false,   
 	 closeOnCancel: false

  });
 });
$(document).ready(function(){
    $("#btnShowAlert").click(function(){
        alert("Submitted");
    });
});

$(document).ready(function(){
    $("form").submit(function(){
        swal("Submitted");
    });
});




 


