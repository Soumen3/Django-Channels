console.log('Java Script connected');

var ws= new WebSocket('ws://localhost:8000/ws/wsc/');

ws.onopen= function(){
    console.log("Connected to the server");
    ws.send('Frontend connected successfully..')
}

ws.onmessage =function(event){
    console.log("Message receive from server...",event['data']);
    document.getElementById('ct').innerText=event.data;
}