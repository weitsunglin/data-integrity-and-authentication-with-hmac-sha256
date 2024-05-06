import hashlib
import hmac

def compute_hmac_sha256_for_zip(item, zip_filepath):
    secret_key = 'your_secret_key_here'  # 在此处替换为您的密钥

    try:
        print("Computing HMAC-SHA256 for ZIP file")
        print("Item:", item)

        # 读取 ZIP 文件内容
        with open(zip_filepath, 'rb') as file:
            file_content = file.read()

        # 创建 HMAC 对象，使用密钥和 ZIP 文件内容
        hmac_obj = hmac.new(secret_key.encode('utf-8'), file_content, digestmod=hashlib.sha256)

        # 获取十六进制格式的校验和
        hex_digest = hmac_obj.hexdigest()
        print("HMAC-SHA256 Digest:", hex_digest)
        return hex_digest

    except Exception as error:
        print("Error during HMAC computation:", error)
        return None

# 示例用法
item_description = "Example ZIP file"
zip_filepath = "test.zip"  # 替换为您的 ZIP 文件路径
compute_hmac_sha256_for_zip(item_description, zip_filepath)
