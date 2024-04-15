console.log("Static connected");

const groupName = JSON.parse(document.getElementById('group-name').textContent);
console.log(groupName);


var ws = new WebSocket('ws://' + window.location.host + '/ws/aschat/' + groupName + '/');

ws.onopen = function () {
    console.log("Connected To Server..");

}
ws.onmessage = function (event) {
    // console.log(event);
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
};

function handleMessage(messageData){
    console.log(messageData);
    document.querySelector("#chat-log").value += (messageData.msg + '\n');
    
}

ws.onclose = function () {
    console.log("Websocket connection closed..");
}

// sending message to server 
document.getElementById('chat-message-submit').onclick = function (event) {
    const messageInputDom = document.getElementById('chat-message-input');
    const message = messageInputDom.value;
    console.log(message);
    ws.send(JSON.stringify({
        'msg': message,
    }))
    messageInputDom.value='';
}