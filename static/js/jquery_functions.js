// Jquery Functions

// get current URL path and assign 'active' class
$(document).ready(function() {
    
    var pathname = window.location.pathname; 
    
    $('#navbarDefault > ul > li > a[href="'+pathname+'"]').parent().addClass('active');
    
});

$(".dropzone").dropzone({
    url: 'upload.php'
});

Dropzone.options.myAwesomeDropzone = {
    paramName: "file", // The name that will be used to transfer the file
    maxFilesize: 2,
    method: "POST",
    acceptedFiles: ".gpx",

}