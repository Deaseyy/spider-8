"""
webpack 打包，非对称加密


载荷加密参数：
    password: "HdIKsgk0jTc+gyPnw0FIW0ojlOZ0bNPZtAF2PxEolOucGP+ELJHZw0WvtfZj9j4xeid4g6dopIYsM4Y6NlOf7WdnZCFgTsltXiw2tPfLz7+70y4QApRYUdLRms8rglm9gqx4QmKzm6RGqWqlyuM8iddNOZbVcriVV3FXkzA09V8="
    - 非对称加密


===== 关键代码

密码加密位置：
o.publicKey && (t.password = o.ec.encrypt(t.password));
分析得到:
o.ec 为webpack 下标为 5 的模块


通过前一个接口 获取 publicKey：
    https://clogin.ke.com/authentication/password/initialize
返回结果：
    {"passwordTicketId":"7xtjKB0K846JWMiJBg8HfL4falVScgTh","publicKey":{"appEncrypt":"false","version":"1","key":"MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCCB81pk1Go/d7K8unYqeB6YyQdDgIRsLji7BxlBfMC2U8/0lyOLxJ6sQb1RmKaILuxN0hRci4zWPfkkPhttWaogq3XABYiDYbx0843ge4D79pG21+qWplw43uHZNs0B6iUChJW1O3DDJPXGwj50L1ySTVt7G7iqsIr9PLZVRSZmQIDAQAB"},"success":true,"supportedIdentityCheckMethods":["old-password","security-code"]}
"""