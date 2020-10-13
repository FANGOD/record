var loading =  require('loading-cli');

var i = 2.5

var load = loading(" 正在准备终端...");

load.frame(["◐", "◓", "◑", "◒"]);

load.start()
setTimeout(function(){
    load.text = " 外部电源接触...没有异常";
},100 * i);
setTimeout(function(){
    load.text = " 思考形态以中文为基准，进行思维连接...";
},200 * i);
setTimeout(function(){
    load.text = " 同步率为 110.00%";
},300 * i);

setTimeout(function(){
    load.text = " 交互界面连接...";
},400 * i);
setTimeout(function(){
    load.text = " 安全装置解除...";
},500 * i);

// stop
setTimeout(function(){
    load.stop();
    console.log("   启动成功！\n");
},600 * i)
