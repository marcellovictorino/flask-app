// Jquery Functions

// get current URL path and assign 'active' class
$(document).ready(function() {
    
    var pathname = window.location.pathname; 
    
    $('#navbarDefault > ul > li > a[href="'+pathname+'"]').parent().addClass('active');
    
})
