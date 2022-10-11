# 文档

## 单元测试

设计思路：对于username，password，mobile和url，检查所有边界条件；对于其他，检查是否存在

实现思路：逐个修改content的key，并使用assertEqual检查

测试用例列表：

* ```json
  {
    "username": 0
  }
  ```
* ```json
  {
    "username": "asd"
  }
  ```
* ```json
  {
    "username": "asd123412341234"
  }
  ```
* ```json
  {
    "username": "123asd"
  }
  ```
* ```json
  {
    "username": "asd123asd"
  }
  ```
* ```json
  {
    "username": "asd123!"
  }
  ```
* ```json
  {
    "username": "asd123"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": 0
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-123123123123123"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123."
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": 0
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": ""
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": 0
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.123"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://asdasdasdasdasd.gwgewgewgewg.scbssbsfsfb.qwrwqeqwewqew.adafasf"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "hhttp://-a.b"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": 0
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.1"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.11111111111111"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+111.111111111111"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.111111111111"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.111111111111",
    "magic_number": 0
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.111111111111",
    "magic_number": "-1"
  }
  ```
* ```json
  {
    "username": "asd123",
    "password": "Asd123-^",
    "nickname": "",
    "url": "http://a.b",
    "mobile": "+11.111111111111",
    "magic_number": "0"
  }
  ```

覆盖率：88%

分析：`import`语句，函数定义语句和常量定义语句未被计入覆盖率

## 集成测试与端到端测试

设计与实现思路：直接复制并修改文档与示例

## Docker部署

设计思路：用三个Docker容器分别保存nginx，app，mysql，nginx把8000端口映射到宿主机8000端口，app暴露5000端口，mysql暴露3306端口，用网络分别连接nginx与app，app与mysql。app使用Dockerfile构建。

心得体会：熟悉了Docker的使用方法，已经可以用Docker构建各种项目。