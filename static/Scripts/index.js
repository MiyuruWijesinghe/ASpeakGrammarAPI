function singlishConvert(){
    var str = $("#InputText").val();
    if(str.length>0){
    dataSend = {"inputText" : $("#InputText").val()}
    console.log(dataSend)
    $.ajax({
        type: "POST",
        url: "/check-grammar",
        data: JSON.stringify(dataSend, null, '\t'),
        contentType: 'application/json;charset=UTF-8',
        success: function (data) {
            console.log(data)
            if(data.isCorrectGrammar === "Wrong grammar"){
                $("#resultGrammar").text("ව්‍යාකරණ වැරදියි");
            }
            if(data.isCorrectGrammar === "Correct grammar") {
                $("#resultGrammar").text("ව්‍යාකරණ නිවැරදියි");
            }
            if(data.tense === "test"){
                $("#resultTense").text("කාලය වැරදියි");
            }
            if(data.tense === "present"){
                $("#resultTense").text("වර්තමාන කාල");
             }
             if(data.tense === "past"){
                $("#resultTense").text("අතීත කාල");
             }
             if(data.numberOfGrammar === "test"){
                $("#numberVal").text("සංඛ්‍යාව වැරදියි");
             }
             if(data.numberOfGrammar === "plural"){
                $("#numberVal").text("බහු වචන");
             }
             if(data.numberOfGrammar === "singular"){
                $("#numberVal").text("ඒක වචන");
             }
             $("#sinhalaString").text(data.sinhalaText);
        },
        complete: function (xhr, textStatus) {
            console.log("AJAX Request complete -> ", xhr, " -> ", textStatus);
        },
        error: function () {
            $("#sinhalaString").text("හරිද ?");
            $("#resultGrammar").text("හරිද ?");
            $("#resultTense").text("හරිද ?");
            $("#numberVal").text("හරිද ?");
            $("#myModal").modal();
            console.log("Error occur");
        }
    });

    }else{
        $("#sinhalaString").text("හරිද ?");
        $("#resultGrammar").text("හරිද ?");
        $("#resultTense").text("හරිද ?");
        $("#numberVal").text("හරිද ?");
        $("#myModal02").modal();
    }
};
