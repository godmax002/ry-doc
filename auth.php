<?php
# 1.生成请求的auth头
$pub_key = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2hbhi7pszx5eN6xqdGBUi4dDm\nNq7Cy//VoMTJVRoblwLQwZ+JKzi5uOfqxdDtJyso+DQzw1Oo0XZtLKSyY7CMnzjf\nwbRMzP5Zt4c2mvU+aL16Aat5riAgJqXS3tTHjulxTQMlTh9jMXc7PgqITBy4IkeV\namvNdumEJ9kzldJzqwIDAQAB\n-----END PUBLIC KEY-----";
$user_id = 1;    # 用户id
$expire = 10000; # 过期时间
$data = array("k2" => "v2", "k1" => "v1");

ksort($data); 
$data_to_sign = json_encode($data);
echo $data_to_sign."<br>";
$data_to_sign = hash("sha256", $data_to_sign);
$data_to_sign = $user_id.':'.$expire.':'.$data_to_sign;
echo $data_to_sign."<br>";

$PK = "";
$PK = openssl_get_publickey($pub_key);
$sign="";
openssl_public_encrypt($data_to_sign,$sign,$PK, OPENSSL_PKCS1_OAEP_PADDING);
$sign = bin2hex($sign);
$auth = $user_id.':'.$expire.':'.$sign;
# auth 即为请求头
echo $auth."<br>";


# 2.校验服务器的auth头
# 服务器post 的数
# post data
$data = array("k2" => "v2", "k1" => "v1");
# auth 头
$auth = '0:10000:9aa10b11a9727b135285669608209685d46c0e7ac02a12220e59772b10d85ab8d658bb2ece71016331c9423f336fff7a6375a94a2ec92fc989a69735fdc1ec904567d1b041624f4beb49b3d208f5394c9f287608b586697101eda33b7611705d0653581057779cf9dc7a9bb1ee5cfd9aa3c4256b6cf5d28b048cebcd356915b8';

$user_id = 0;
$expire = 10000;
$sign = '416def8aabf49d07313f7d9edbf9fa63158fb5216c05a1dc15d3fcf3fa3dfdd35eefdc55e519b1717384aade468349a401a480ed0d8f92d4ae8093d02ddd10f8bf3223272c4c0575db749ebc4929f94d9185d3a55579f7c4c1baba90f98f18e017d5f36e7d5565bacefcc7cd08f1b6b103627449e1b55f879d1e8f222e57b462';

ksort($data);
$data_to_sign = json_encode($data);
$data_to_sign = hash("sha256", $data_to_sign);
$data_to_sign = $user_id.':'.$expire.':'.$data_to_sign;
echo $data_to_sign."<br>";
$sign = hex2bin($sign);
$is_valid = openssl_public_decrypt($sign, $data_to_sign, $pub_key);
echo $is_valid ? 'true' : 'false';
?>
