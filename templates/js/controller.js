//https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse

if (window.addEventListener) {

    var canvas, context, tool;

    window.addEventListener('load', function () {

        function init() {
            canvas = document.getElementById('imageView');
            context = canvas.getContext('2d');
            context.fillStyle="#FFFFFF";
            context.fillRect(0, 0, 400, 300)

            tool = new tool_pencil();

            canvas.addEventListener('mousedown', ev_canvas, false);
            canvas.addEventListener('mousemove', ev_canvas, false);
            canvas.addEventListener('mouseup', ev_canvas, false);

        }
        function tool_pencil() {
            var tool = this;
            this.started = false;

            this.mousedown = function (ev) {
                context.beginPath();
                context.moveTo(ev._x, ev._y);
                tool.started = true;
            };
            this.mousemove = function (ev) {
                if (tool.started) {
                    context.lineTo(ev._x, ev._y);
                    context.lineWidth = 15;
                    context.stroke();

                }
            };

            this.mouseup = function (ev) {
                if (tool.started) {
                    tool.mousemove(ev);
                    tool.started = false;
                }
            };
        }

    
        function ev_canvas(ev) {
                ev._x = ev.layerX;
                ev._y = ev.layerY;
                ev._x = ev.offsetX;
                ev._y = ev.offsetY;
            }

            // Call the event handler of the tool.
            var func = tool[ev.type];
            if (func) {
                func(ev);
            }
        }

        init();

    }, false);
}

document.getElementById('clear').addEventListener('click', function () {
    context.fillStyle="#FFFFFF";
    context.fillRect(0, 0, 400, 300)

    
}, false);

function saveDrawing() {

    var img = canvas.toDataURL("images/png");

    $.ajax({
        url: '/upload',
        method: 'POST',
        data: img,
        success: function (res) {
            console.log(res);
            $('#prediction').text( res);

        }, error: function (err) {
            console.log(err);
        }
    });
}
