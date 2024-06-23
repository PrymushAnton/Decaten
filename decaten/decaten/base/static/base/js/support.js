$("#inputs button").css("height", `${($(window).height()/100)*10}px`)
$("#inputs textarea").css("height", `${$("#inputs button").height()}px`)
$("#inputs").css("margin-left", `${($(window).height()/100)*2}px`)
$("#body").remove("#footer")
$("footer").remove()
var messages = [{"role" : "assistant", "content" : "Привіт! Як я вам можу допомогти?"}]
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
        $(".space").remove()
        $("#chat").append(`
            <div class="message1">
                <p>${$("#exampleFormControlTextarea1").val()}</p>
            </div>
        `)
        $("#chat").append(`
            <div class="space1">
                <p class="card-text placeholder-glow">
                <span class="placeholder col-7"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-6"></span>
                <span class="placeholder col-8"></span>
                </p>
            </div>
        `)
        $("#chat").append(`
            <div class="space">
            </div>
        `)
        $("#exampleFormControlTextarea1").val("")
        $.ajax({
            url:$("#support").val(),
            type: "POST",
            headers: { "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val() },
            data: {"messages" : messages},
            success: function(response){
                console.log("fetched")
                $(".space").remove()
                $(".space1").remove()
                $("#chat").append(`
                <div class="message">
                    <p>${response["answer"]}</p>
                </div>
                `)
                $("#chat").append(`
                    <div class="space">
                    </div>
                `)
            }
        })
    });
});
