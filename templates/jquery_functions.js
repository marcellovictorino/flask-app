// Jquery Functions

// get current URL path and assign 'active' class
$(document).ready(function() {
    
    var pathname = window.location.pathname; 
    
    $('.nav > div > ul > li > a[href="'+pathname+'"]').parent().addClass('active');
    
})

function test(){
    console.log("Function has been run")
}