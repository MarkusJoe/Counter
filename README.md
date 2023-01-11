<div style="text-align: center">

Demo

![Counter](https://count.rtast.cn/MoeCounter)

</div>

# py 版访问次数计数器

> 翻自 [journey-ad](https://github.com/journey-ad/Moe-counter) 的计数器

# 新特性

* 使用了异步Web框架`FastAPI`来提高效率, 所有代码均为异步操作
* 可以自定义显示图片的数量(长度)
* 支持API接口以便自行开发
* 支持了`MySQL`数据库

# 失去的特性

* 暂未支持`MongoDB`

# 安装 & 运行

```bash
$ pip3 install -r requirements.txt
$ uvicorn src:create_app --factory  or 
$ sh run.sh  or
$ python3 main.py  # 两条命令等价
```

# 部署到Vercel

> 部署到Vercel之前请先 `fork` 本仓库, 修改 `.env` 文件内的PJ_DETA将其更换成你自己的 `Deta Project Key` 你也可以直接使用默认的

# 部署到Deta

> 部署到Deta后将使用Deta的Base数据库

* ***你需要提前准备一个Deta账号***
* [![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/RTAkland/MoeCounter)

# 开源

- 本项目以[Apache-2.0](./LICENSE)许可开源, 即:
    - 你可以直接使用该项目提供的功能, 无需任何授权
    - 你可以在**注明来源版权信息**的情况下对源代码进行任意分发和修改以及衍生

## 鸣谢

* [JetBrains](https://www.jetbrains.com/zh-cn/) 提供强大的IDE支持