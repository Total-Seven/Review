// 获取用户输入
process.stdin.resume();
process.stdin.setEncoding('utf8');

console.log("请输入一些内容：");

process.stdin.on('data', function (data) {
    // 处理用户输入
    console.log("你输入的内容是：" + data.trim());

    // 结束输入流
    process.stdin.pause();
});
