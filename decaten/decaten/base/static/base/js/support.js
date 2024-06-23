$("#inputs button").css("height", `${($(window).height()/100)*10}px`)
$("#inputs textarea").css("height", `${$("#inputs button").height()}px`)
$("#inputs").css("margin-left", `${($(window).height()/100)*2}px`)
$("#body").remove("#footer")
var messages = []
$(document).ready(function() {
    $("#inputs button").on("click", function(){
        messages.push({"role" : "user", "content" : $("#exampleFormControlTextarea1").val()})
        console.log("fetching")
        // fetch("https://automatic-funicular-gjrvpqqjp7xfwjxp-8000.app.github.dev/", {
        //     method: "POST", 
        //     mode: 'no-cors',
        //     // headers: {
        //     //     'Content-Type': 'application/json'
        //     // },
        //     body: JSON.stringify({
        //         "messages": messages,
        //         // Note: Access-Control-* headers cannot be set via the body of a request when using Fetch API.
        //         // They must be set server-side or through CORS configuration.
        //     })
        // })
        // .then(response => response.json())
        // .then(data => {
        //     console.log("success");
        //     console.log(data);
        // })
        // .catch((error) => {
        //     console.error('Error:', error);
        // })
        $.ajax({
            url:"https://automatic-funicular-gjrvpqqjp7xfwjxp-8000.app.github.dev/",
            type: "GET",
            data: {"messages" : messages},
            headers: {
                'Content-Type':'application/json'
            },
            dataType: "jsonp",
            success: function(data){
                console.log('succes: '+data);
            }
        })
    });
});
