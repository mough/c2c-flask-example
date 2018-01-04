$(document).ready(function(){
    console.log("I was correctly initied");
    $("#search-submit").click(function(event) {
        
        event.preventDefault();

        var recipeCategory = $("#category").val();
        var recipeName = $("#name").val();
        var recipeUrl = $("#url").val();

        var queryString = "/recipes" + "?name=" + recipeName + "&category=" + recipeCategory + "&url=" + recipeUrl;
        
        $.getJSON( queryString, function (json) {
            console.log(json);
            
            var items = [];
            items.push("<ul>");

            $.each( json, function( key, val ) {
                items.push( "<li>" + "Name = " + val.name + " | " + "Url = " + val.url + " | " + "Category = " + val.category + "</li>" );
            });
            items.push("</ul>");            
            $("#searchResults").html(items);
        });
    });
});