console.log("Script connected");

const groupName = JSON.parse(document.getElementById("group_name").textContent);
console.log("Group name: ", groupName);


var ws = new WebSocket('ws://' + window.location.host + '/ws/aschat/' + groupName + '/');

ws.onopen = function () {
    console.log("Websocket Connected....");
}

ws.onmessage = function (event) {
    // console.log('Message from server:', event);
    var data = event.data;
    if (typeof data === "string") {
        try {
            const messageData = JSON.parse(data);
            handleMessage(messageData);
        } catch (e) {
            alert(`Invalid server response: ${e}`);
            }
    } else {
        alert('Received binary message, but expected text!')
    }
    
}

ws.onclose = function (event) {
    console.log("Websocket Disconnected....", event);
}


document.getElementById('chat-message-submit').onclick= function(){
    const messageDOM=document.getElementById('chat-message-input');
    const message=messageDOM.value;
    ws.send(JSON.stringify({
        'msg':message
    }));
    messageDOM.value='';
};


function handleMessage(messageData){
    console.log(messageData);
    document.querySelector("#chat-log").value += (messageData.msg + '\n');
    
}

