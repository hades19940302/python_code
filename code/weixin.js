wx.chooseImage({
  success: function (res) {
    var tempFilePaths = res.tempFilePaths
    wx.uploadFile({
      url: 'https://ai.kilig.com.cn/test/',
      filePath: tempFilePaths[0],
      name: 'picture',
      success: function (res) {
        var jsonText = JSON.parse(res.data);
        var data = res.data;
        var translation = res.data.translation;
        wx.showModal({
          title: 'what',
          content: jsonText['translation'][0],
        })
        //do something
      }
    })
  }
})