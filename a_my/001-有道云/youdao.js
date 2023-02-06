var crypto = require('crypto');
// var CryptoJS = require('crypto-js');


var o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl';
var n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4';

function decodeData(sign) {
    const key = crypto.createHash("md5").update(o).digest();
    const iv = crypto.createHash("md5").update(n).digest();

    const cipher = crypto.createDecipheriv('aes-128-cbc', key, iv);
    let src = cipher.update(sign, 'base64', 'utf-8');
    src += cipher.final('utf-8');
    return src;
}

// test
const sign = 'Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6qaEgNoL9hpcSmEB6685K2g_6vKeCBoW_2onZCm9lcoW72YMQC6Jro7XuC0JjLRpW8YWrbe_H5Q-LIw1uO3YX2gUY1_6yqDNn4rvl2Tc-axk3N0u3pnPLnWWnQXdNTf61BnpEC0RyZRlOKXldTcAIJ_zhnJuizmcFry5IpEFFDLMeDwOKRpmDqGqT7WeFIdXybr-vkmjPGdsYfb6wG76MlwV2vc7bTM_AXswRKDFxoCexbmCGNtplR8OZQ0JFy0hlZvAMqtQ21g-CnSW7gDLEYvq5Ry4t0hF_ykgWBvNnruZDOQXolhsrcVbmpwvTDQQY81Wiw3bIEvjE_mgEcHvmqg1xeguHjDuFaYSnl9FXr_e2w47TpEa4AwoRT6-VnFVxGkiyfbPFtbTJRr21JoacqE9ecLzGUX1GJfTEdcnFjorCt1B4Gz7wXGZiyED4CPQrDfz8m7-WTzvaYXHF0jKFqAfW6oO9mU1q-5CsySBJ5F4cXivBwWaMWOrcgKZflKvR_Jt5dBokbn2N2sZsXur3BZWHEJ2sRiWwK-jE0_eXsXoL6rYr4niXNX4MtDZoBMFn1nzIZYUwMd9fg97hOPN8aza5nJvkYcRG4zEOZsHV1ZpO7iDJHDadi_NlQrQ7pyHVt9RewNj0MUAMmUfMiUExQXO2NT5_CK3daDsSC1FxWV264W4K_tfB-RE_yv_2ErGBEveR-ZrYe6EFq1gILxfMz36Lf-7U_Gtpbcwz9jtBs0Cyst4pPIi0dhkrTbrYEyok5kyj4-GY7GsQcSOGBL9SZCTql3i-MsjQIs-8JrVVKmU='
console.log(decodeData(sign));

