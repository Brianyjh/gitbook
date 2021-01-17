##### 创建文件夹

```bash
mkdir hello
```

```bash
cd hello
```

```bash
git init
```
##### 克隆已有项目

```bash
git clone https://github.com/Brianyjh/gitbook.git
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210117224815844.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTUzNjkzNg==,size_16,color_FFFFFF,t_70)
不过，github实在是太慢了，我们可以把GitHub上的仓库导入到国内的 Gitee上![在这里插入图片描述](https://img-blog.csdnimg.cn/20210117225008679.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTUzNjkzNg==,size_16,color_FFFFFF,t_70)

然后

```bash
git clone https://gitee.com/brianyjh/gitbook.git
```
克隆完毕后，进入文件夹执行

```bash
git remote -v
```
查看指向远端仓库的地址
修改为github的地址

```bash
git remote set-url origin https://github.com/Brianyjh/gitbook
```

