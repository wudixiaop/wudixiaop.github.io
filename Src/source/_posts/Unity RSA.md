title: Unity + openssl 生成的 RSA 秘钥实现可靠的简单数据加密
date: 2016-03-01 15:56:56
tags: Security  
category: Unity
---

现实中会有很多需求，对数据加密是其中一种。我们对数据的加密方式有 __对称加密__ 和 __不对称加密__。对称加密就是使用相同的秘钥和算法加密明文和解密密文。
而不对称加密，就是有加密和解密使用不同秘钥的算法，其中对外公开的叫 __公钥__（public key），不公开的叫 __密钥__（private key）。
本文中要提到的 RSA 算法就是一种不对称加密算法。

### RSA 介绍
关于 RSA, 详细介绍 [请看这里](http://baike.baidu.com/view/10613.htm?fromtitle=RSA&fromid=210678&type=syn)。

### RSA 秘钥生成  

上面提到RSA 是不对称算法，它有 public key 和 private key，下面我们用 openssl 来生成它们。下面使用 OSX 系统上自带的 openssl 来生成秘钥。

> __➜  ~ openssl__    
> __OpenSSL> genrsa -out rsa_private_key.pem 1024__  
> Generating RSA private key, 1024 bit long modulus  
> ..........++++++  
> ........................++++++  
> e is 65537 (0x10001)  
> __OpenSSL> pkcs8 -topk8 -inform PEM -in rsa_private_key.pem -outform PEM -nocrypt__  
> -----BEGIN PRIVATE KEY-----  
> MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKGhqNRI8ygdZcsW  
> FofWo0+ERSJSQDIjDCrkWlDkKmQP3miYs0ARb00ik95z3IIRp0NCSmDJMRS2Gjdj  
> jNXlHNLZOw05OtH+47Hi3IGmi+dFDzPgux4KzXfs5eOXkhLfSR7XQ2ju1A5q6lAw  
> mXFR8IqEMR73EbwXZM6GHmMC0yglAgMBAAECgYAffJ2mFTwBQZDV+kyTU9XmpK7P  
> G9TTr44sQOXzQi+b5JeAKtcokPzsuuKxgEKhuAyshpp0tlzwWvVKewMxm/t8LIEq  
> O7rwk4w/9Hx5CX+gOogOc6HnjEAucUqr9qxBIsKyvt7V+PlZmytnIamnV3GA7fVV  
> O0APf1DtkU30eGnlAQJBAM2UMpOBwvBchWiYymnRtCyCf7qPGrbNb748a12Ca9Fc  
> eEqdH3FQGBSAUX2xij6exhGAHVPCIfwe9p+A2UTFMGUCQQDJRhwjZ0gnec8pjECX  
> hzaulzsu96ypXZltYaOsArP3pnrD4VzNy8aaplgwMXPBl3/sDyAQkRiLg4ExUUk1  
> ajzBAkB9EZ8fbH9ree5T7zid3k2uEoqgtjU7Z4qHAv0Su6jai1ZHloWti1vLBTIO  
> tTd012WK+hVdgqroVvIVoe8MzqadAkEAnD0RMKZGy2Xx2uWlajqqxuJcLbxSynH+  
> 3Hqzq525h98yYwV4ncO2GmxP/rEUk02AHoUrNdD8BaiCS/82XgFmwQJAdCbcdxFK  
> ZUVK3+OCGretEHdedWuVPXEhfiLDpguog994jdoCMCmGviKiOURNo3QsK5DfT0+A  
> Lw307ILOc1dqcg==  
> -----END PRIVATE KEY-----  
> __OpenSSL> rsa -in rsa_private_key.pem -pubout -out rsa_public_key.pem__  
> writing RSA key  
> __OpenSSL>__   

然后 openssl 会为我们生成两个文件，分别叫做 __rsa_private_key.pem__ 和 __rsa_public_key.pem__。

### 与 Unity 结合

这里，我们引入一个类叫做 [RSACryptoServiceProvider](https://msdn.microsoft.com/zh-cn/library/system.security.cryptography.rsacryptoserviceprovider%28v=VS.110%29.aspx), 它是 .NET 提供的类。需要说明的是，它不能直接使用 openssl 生成的 pem 文件，我们需要转换 pem 到它能使用的格式，也就是 RSAParameters 类。具体算法那如下代码所示：

{% codeblock %}
using System.Security.Cryptography;
using System.Text;
using System;

public class RSAHelper
{
    public static string Encript(string value, string pemPublicKey)
    {
        using(RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(ConvertFromPemPublicKey(pemPublicKey));
            var encryptedBytes = rsa.Encrypt(Encoding.UTF8.GetBytes(value), false);
            return Convert.ToBase64String(encryptedBytes);
        }
    }
    
    public static string Decrypt(string encryptedData, string pemPrivateKey)
    {
        using(RSACryptoServiceProvider rsa = new RSACryptoServiceProvider())
        {
            rsa.ImportParameters(ConvertFromPemPrivateKey(pemPrivateKey));
            var data = rsa.Decrypt(Convert.FromBase64String(encryptedData), false);
            return Encoding.UTF8.GetString(data, 0, data.Length);
        }
    }
    
    // http://blog.csdn.net/liguo9860/article/details/40922919
    //
    public static RSAParameters ConvertFromPemPublicKey(string pemFileConent)  
    {  
        pemFileConent = pemFileConent.Replace("-----BEGIN PUBLIC KEY-----", "").Replace("-----END PUBLIC KEY-----", "").Replace("\n", "").Replace("\r", "");  
        byte[] keyData = Convert.FromBase64String(pemFileConent);  
        bool keySize1024 = (keyData.Length == 162);  
        bool keySize2048 = (keyData.Length == 294);  
        if (!(keySize1024 || keySize2048))  
        {  
            throw new ArgumentException("pem file content is incorrect, Only support the key size is 1024 or 2048");  
        }  
        byte[] pemModulus = (keySize1024 ? new byte[128] : new byte[256]);  
        var pemPublicExponent = new byte[3];  
        Array.Copy(keyData, (keySize1024 ? 29 : 33), pemModulus, 0, (keySize1024 ? 128 : 256));  
        Array.Copy(keyData, (keySize1024 ? 159 : 291), pemPublicExponent, 0, 3);  
        var para = new RSAParameters { Modulus = pemModulus, Exponent = pemPublicExponent };  
        return para;  
    }  
    
    // http://blog.csdn.net/liguo9860/article/details/40922919
    //
    public static RSAParameters ConvertFromPemPrivateKey(string pemFileConent)
    {
        if (string.IsNullOrEmpty(pemFileConent))
        {
            throw new ArgumentNullException("pemFileConent", "This arg cann't be empty.");
        }
        
        pemFileConent = pemFileConent.Replace("-----BEGIN RSA PRIVATE KEY-----", "").Replace("-----END RSA PRIVATE KEY-----", "").Replace("\n", "").Replace("\r", "");
        byte[] keyData = Convert.FromBase64String(pemFileConent);
        bool keySize1024 = (keyData.Length == 609 || keyData.Length == 610);
        bool keySize2048 = (keyData.Length == 1190 || keyData.Length == 1192);

        if (!(keySize1024 || keySize2048))
        {
            throw new ArgumentException("pem file content is incorrect, Only support the key size is 1024 or 2048");
        }

        int index = (keySize1024 ? 11 : 12);
        byte[] pemModulus = (keySize1024 ? new byte[128] : new byte[256]);
        Array.Copy(keyData, index, pemModulus, 0, pemModulus.Length);

        index += pemModulus.Length;
        index += 2;
        var pemPublicExponent = new byte[3];
        Array.Copy(keyData, index, pemPublicExponent, 0, 3);

        index += 3;
        index += 4;
        if (keyData[index] == 0)
        {
            index++;
        }
        byte[] pemPrivateExponent = (keySize1024 ? new byte[128] : new byte[256]);
        Array.Copy(keyData, index, pemPrivateExponent, 0, pemPrivateExponent.Length);

        index += pemPrivateExponent.Length;
        index += (keySize1024 ? ((int)keyData[index + 1] == 64 ? 2 : 3) : ((int)keyData[index + 2] == 128 ? 3 : 4));
        byte[] pemPrime1 = (keySize1024 ? new byte[64] : new byte[128]);
        Array.Copy(keyData, index, pemPrime1, 0, pemPrime1.Length);

        index += pemPrime1.Length;
        index += (keySize1024 ? ((int)keyData[index + 1] == 64 ? 2 : 3) : ((int)keyData[index + 2] == 128 ? 3 : 4));
        byte[] pemPrime2 = (keySize1024 ? new byte[64] : new byte[128]);
        Array.Copy(keyData, index, pemPrime2, 0, pemPrime2.Length);

        index += pemPrime2.Length;
        index += (keySize1024 ? ((int)keyData[index + 1] == 64 ? 2 : 3) : ((int)keyData[index + 2] == 128 ? 3 : 4));
        byte[] pemExponent1 = (keySize1024 ? new byte[64] : new byte[128]);
        Array.Copy(keyData, index, pemExponent1, 0, pemExponent1.Length);

        index += pemExponent1.Length;
        index += (keySize1024 ? ((int)keyData[index + 1] == 64 ? 2 : 3) : ((int)keyData[index + 2] == 128 ? 3 : 4));
        byte[] pemExponent2 = (keySize1024 ? new byte[64] : new byte[128]);
        Array.Copy(keyData, index, pemExponent2, 0, pemExponent2.Length);

        index += pemExponent2.Length;
        index += (keySize1024 ? ((int)keyData[index + 1] == 64 ? 2 : 3) : ((int)keyData[index + 2] == 128 ? 3 : 4));
        byte[] pemCoefficient = (keySize1024 ? new byte[64] : new byte[128]);
        Array.Copy(keyData, index, pemCoefficient, 0, pemCoefficient.Length);

        var para = new RSAParameters
            {
                Modulus = pemModulus,
                Exponent = pemPublicExponent,
                D = pemPrivateExponent,
                P = pemPrime1,
                Q = pemPrime2,
                DP = pemExponent1,
                DQ = pemExponent2,
                InverseQ = pemCoefficient
            };
        return para;
    }
}

{% endcodeblock %}

然后我们可以直接调用 `RSAHelper.Encript` 来加密数据，`RSAHelper.Decrypt` 解密数据。如下面代码，`Encode()` 加密 `Hello Rocky` 字符串，然后 `Decode()` 解决加密后的字符串。

{% codeblock %}
using UnityEngine;
using UnityEngine.UI;
using System;

public class Sample : MonoBehaviour {

    public Text output;
    
    private string publicKey = @"-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzVBO/HUhgU4cIRS2UE255r2uG
EaVuPAxrANab5z7rv/hUm1t1TW9G6qaLvXraUS2c6m4PW+VVY8j/fViIy9XLhd2I
dYsbuTNyV6gQVnA4tdMdnJdrvfzaXiIoPzP3u9Ll8LEQSW2iiludxwBlVz/VdCiA
EYBMuYmrmSHsan5ObQIDAQAB
-----END PUBLIC KEY-----";
    
    private string privateKey = @"-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCzVBO/HUhgU4cIRS2UE255r2uGEaVuPAxrANab5z7rv/hUm1t1
TW9G6qaLvXraUS2c6m4PW+VVY8j/fViIy9XLhd2IdYsbuTNyV6gQVnA4tdMdnJdr
vfzaXiIoPzP3u9Ll8LEQSW2iiludxwBlVz/VdCiAEYBMuYmrmSHsan5ObQIDAQAB
AoGBAIHSy1zfQSdjMO2ez0lU6/SyN0BfBAmS9VZ9y+AgACBB4PC3a/W28mk/tQST
Tx5ACKqB2N3LpHI2BCxaPT8DeilfjaUibpOqXJ918+oXmOEpEBpEz2FzkzZWeUOo
8bkDiuEE1RyzQEQExxCbiLQFCpX0NNIpccrTYJ3wRZfroojNAkEA4Pd9xxscmxQM
s4aQgE+/paQWR//B2JQjhsxvYfLhrMUKgWMWpfm5EfhG3AlIE/N7iZADPLZ+2JMG
2ljnE3VdzwJBAMwQ6DJpueg2Yj5+ufTVhFBIkJZXWGIZv5FWmzaycfJOafg/ToRB
QWjU7Dr7buxQ4jgFI6eZcN8uM5pcer/ouwMCQDRCSb2O1r5PkgPCJp8n52UbEPH4
v5cIEpiltNoUCciQnTghRImZ0RwTiKJkpZG85d22zomz+xNkVBs0u7kRcpECQAfH
NTKGuSFSwVfkeK4OXWa5/Vjdp27F0Hl3tZ7WGmXD+2IM968u1ZFrXD27S7USOC0u
dPd0b8rx9eGSWNNryYUCQQCWbiNhKEDQ1+yauWhZwamsc2Zl/Gde0eQYrWlmoZRE
r4w8Xlt8XVBTNBf5ljALeVtXOs0LNuWqnmy1v7wMPvnN
-----END RSA PRIVATE KEY-----";
    
    void Start()
    {
        output.text = "Hello Rocky";
    }    
    
    
	public void Encode()
    {
        output.text = RSAHelper.Encript("Hello Rocky", publicKey);
    }
    
    public void Decode()
    {
        var data = RSAHelper.Decrypt(output.text.Trim(), privateKey);
        Debug.Log(data);
        output.text = data;
    }
}

{% endcodeblock %}

本文的代码也可以在这里找到： <https://github.com/wudixiaop/UnityRSA>。

Enjoy!