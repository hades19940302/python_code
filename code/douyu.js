var setContent = '小程序搜AI识别图..';
var setIntervalTime = 20;
var setTimes = 10000;
var realTime = 1;
var realContent = setContent;
var realIntervalTime
var autoSendMsg;
var $sendButton = $('div[data-type="send"],#sendmsg_but');
sendMsg();
function sendMsg() {
    if (!checkCanSend()) {
        return;
    }
    realContent = setContent + '-' + realTime++;
    $('textarea').val(realContent);
    $sendButton.click();
    var roomMsgCd = getRoomMsgCd();
    if (roomMsgCd > setIntervalTime) {
        realIntervalTime = roomMsgCd;
    } else {
        realIntervalTime = setIntervalTime;
    }
    autoSendMsg = setTimeout("sendMsg()", realIntervalTime * 1000 + 300);
    realContent = setContent;
    if (realTime > setTimes) {
        clearTimeout(autoSendMsg);
    }
}
function getRoomMsgCd() {
    if (!isNaN(Number($sendButton.text()))) {
        return Number($sendButton.text());
    } else {
        getRoomMsgCd();
    }
}
function checkCanSend() {
    if ($('div[data-type="send"]').hasClass("b-btn-gray")) {
        $('a[data-type="login"]').click();
        return false;
    } else {
        return true;
    }
}
$('textarea').dblclick(function() {
    clearTimeout(autoSendMsg);
});