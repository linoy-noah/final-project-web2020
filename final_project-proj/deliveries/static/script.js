var select
var tableBody
var mails
var gifts
var flowers
var mysteryBoxs
var foods

function hideAll(){
    var c = tableBody[0].children.length;
    for(var i=0;i<c;i++){
        tableBody[0].children[i].style.display="none"
    }
}
function showAll(){
    var c = tableBody[0].children.length;
    for(var i=0;i<c;i++){
        tableBody[0].children[i].style.display="table-row"
    }
}

function showMail(){
    hideAll()
    for(var i=0;i<mails.length;i++){
        mails[i].style.display="table-row"
    }
}

function showFlower(){
    hideAll()
    for(var i=0;i<flowers.length;i++){
        flowers[i].style.display="table-row"
    }
}

function showGift(){
    hideAll()
    for(var i=0;i<gifts.length;i++){
        gifts[i].style.display="table-row"
    }
}

function showFood(){
    hideAll()
    for(var i=0;i<foods.length;i++){
        foods[i].style.display="table-row"
    }
}

function showMysteryBox(){
    hideAll()
    for(var i=0;i<mysteryBoxs.length;i++){
        mysteryBoxs[i].style.display="table-row"
    }
}

window.onload = function(){
    select=this.document.getElementById("sel2")
    tableBody=this.document.getElementsByTagName("tbody")
    mails = document.getElementsByClassName("MA")
    gifts= document.getElementsByClassName("GF")
    flowers= document.getElementsByClassName("FL")
    mysteryBoxs= document.getElementsByClassName("MB")
    foods= document.getElementsByClassName("FO")

    select.onchange = function(){
        console.log(this.value)
        if(this.value == "all"){
            showAll()
        }
        if(this.value=="food"){
            showFood()
        }
        if(this.value=="mail"){
            showMail()
        }
        if(this.value=="flowers"){
            showFlower()
        }
        if(this.value=="gift"){
            showGift()
        }
        if(this.value=="mysteryBox"){
            showMysteryBox()
        }
    }
}