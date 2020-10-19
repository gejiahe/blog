// 1. 下载并导入kinderitor文件
// 2. 新建并编辑config.js文件
KindEditor.ready(function(K) {
                // textarea[name=content]
                K.create('#id_content',{
                    width:'800px',
                    height:'200px',
                    // 图片上传路径
                    uploadJson: '/admin/upload/kindeditor',
                });
        });
