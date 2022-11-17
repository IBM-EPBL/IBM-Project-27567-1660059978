function talk(){
    var know = {
    "Hi" : "Hello ",
    "What say about your smart fashion?" : "This shopping hall is 2011 is start in smart fashion shopping and all vertical dress available.",
    "What about your dress collection?" : "Court and shirts, Sarees, Jean Pants, Kid's Dress, ect...",
    "How to Purchasing?" : "Your see the top navbar, click on purchase button then you have purchasing dresses.",
    "Your followers" : "I have my family of 5000 members, i don't have follower ,have supportive Famiy ",
    "ok" : "Thank You So Much ",
    "Bye" : "Okay! Will meet soon.."
    };
    var user = document.getElementById('userBox').value;
    document.getElementById('chatLog').innerHTML = user + "<br>";
    if (user in know) {
    document.getElementById('chatLog').innerHTML = know[user] + "<br>";
    }else{
    document.getElementById('chatLog').innerHTML = "Sorry,I didn't understand <br>";
    }
    }