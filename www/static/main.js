$(function(){

    var frame_handler = function(socketHandler){
        this.socketHandler = socketHandler;
        var mouse_btn = this.mouse_button_status = [false, false, false, false, false];

        var frame_target = ".frame";

        var percent = this.percent = function(value, max){
            return value / max;
        };
        var offsetPercent = this.offsetPercent = function(x, y, width, height){
            return {
                x: percent(x, width),
                y: percent(y, height),
            };
        };

        $(frame_target).mousemove(function(e){
//            $(this).html(""+e.offsetX+", "+e.offsetY+", "+e.button+", "+e.buttons);
//            console.log(e);
            if (socketHandler){
                width = $(".frame").width()+1;
                height = $(".frame").height()+1;
                socketHandler["MOUSE_MOVE"](offsetPercent(e.offsetX, e.offsetY, width, height));
            }
        });
        $(frame_target).mousedown(function(e){
            $(this).html("mouse down "+e.offsetX+", "+e.offsetY+", "+e.button+", "+e.buttons);
            mouse_btn[e.button] = true;
            console.log(mouse_btn);
            if (socketHandler){
                width = $(".frame").width()+1;
                height = $(".frame").height()+1;
                param = offsetPercent(e.offsetX, e.offsetY, width, height);
                param['button'] = e.button;
                socketHandler["MOUSE_DOWN"](param);
            }
        });
        $(frame_target).mouseup(function(e){
            $(this).html("mouse up "+e.offsetX+", "+e.offsetY+", "+e.button+", "+e.buttons);
            mouse_btn[e.button] = false;
            console.log(mouse_btn);
            if (socketHandler){
                width = $(".frame").width()+1;
                height = $(".frame").height()+1;
                param = offsetPercent(e.offsetX, e.offsetY, width, height);
                param['button'] = e.button;
                socketHandler["MOUSE_UP"](param);
            }
        });

        $(frame_target).bind('mousewheel', function(e){
            if(e.originalEvent.wheelDelta /120 > 0) {
                $(this).text('scrolling up !');
            }
            else{
                $(this).text('scrolling down !');
            }
            console.log(e.originalEvent.wheelDelta);
            if (socketHandler){
                width = $(".frame").width()+1;
                height = $(".frame").height()+1;
                param = offsetPercent(e.offsetX, e.offsetY, width, height);
                param['delta'] = e.originalEvent.wheelDelta;
                socketHandler["MOUSE_WHEEL"](param);
            }
        });
        $(frame_target).click(function(e){
//            $(this).html("click "+e.offsetX+", "+e.offsetY);
//            console.log(e);
        });
        $(frame_target).keydown(function(e){
            $(this).html("key down "+e.keyCode+", shift:"+e.shiftKey+", ctrl:"+e.ctrlKey+", alt:"+e.altKey+", meta:"+e.metaKey);
            param={
                keycode: e.keyCode
            }
            socketHandler["KEY_DOWN"](param);
            e.preventDefault();
            return false;
        });
        $(frame_target).keyup(function(e){
            $(this).html("key up "+e.keyCode+", shift:"+e.shiftKey+", ctrl:"+e.ctrlKey+", alt:"+e.altKey+", meta:"+e.metaKey);
            param={
                keycode: e.keyCode
            }
            socketHandler["KEY_UP"](param);
            e.preventDefault();
            return false;
        });

        // trigger right click
        $(document).on("contextmenu", frame_target, function(e){
            console.log("right click");
            return false;
        });
        this.socketHandler = socketHandler;
    };

    var websocket_function = function(){
        var host = location.host;
        if (host == "") host = "localhost:8888";
        this.ws = new WebSocket("ws:" + host + "/websocket");
        var wsAlive = 0;

        var pingInterval = 30*1000;
        var pingCount = 0;

        this.ws.onopen = this.onopen = function(){
            var data = {
                command: "RETRIVE_HISTORY",
            };
            this.send(JSON.stringify(data) );
            wsAlive = new Date();
            setInterval(function(){
                var data = {
                    command: "SCREEN",
                    payload: {
                        width:  400*2,
                        height: 300*2,
                    }
                };
                this.ws.send(JSON.stringify(data) );
            }, 1000, ws);
            setTimeout(sendPing, pingInterval, ws);
        }

        this.ws.onmessage = this.onmessage = function(evt){
            var data = JSON.parse(evt.data);
            var command = data.command;
            console.log('websocket command', command);

            switch(command){
                case "SCREEN":
                    var payload = data.payload;
                    $('div.frame').css({
                        'background-image':'url("data:image/webp;base64,'+payload+'")',
                    });
                    break;

                case "PONG":
                    console.log('PONG');
                    setTimeout(sendPing, pingInterval, ws);
                    break;

                default:
                    console.log('unknown command: ' + command);
                    break;
            }
        }
        this.onclose = function(){
            //alert('disconnected.');
        }

        var func_array=[
            "MOUSE_MOVE", "MOUSE_DOWN", "MOUSE_UP", "MOUSE_WHEEL", "KEY_DOWN", "KEY_UP"
        ];
        this.sendEventFunctions = [];
        for(var i=0; i<func_array.length; i++) {
            (function(fname){
                this.sendEventFunctions[fname] = function(payload){
                    var command = fname;
                    sendCommand(command, payload)
                }
            }(func_array[i]));
        }

        this.sendCommand = function(command, payload){
            var data = {
                command: command,
                payload: payload
            };
            this.ws.send(JSON.stringify(data));
        }

        function sendPing(ws){
            wsAlive = new Date();
            var data = {
                command: "PING",
            };
            ws.send(JSON.stringify(data) );
        }

        return this.sendEventFunctions;
    }

    var handler = websocket_function();
    frame_handler(handler);
});
