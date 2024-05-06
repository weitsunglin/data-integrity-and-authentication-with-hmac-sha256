import hashlib
import hmac

def compute_hmac_sha256(item, file_content):
    secret_key = 'your_secret_key_here'  # Hardcoded secret key
    try:
        print "Computing HMAC-SHA256"
        print "Item:", item

        # In Python 2.7, strings can be used directly for binary data
        # If file_content is unicode, it needs to be encoded to a byte string
        if isinstance(file_content, unicode):
            file_content = file_content.encode('utf-8')

        # Create an HMAC object using the secret key and file content
        hmac_obj = hmac.new(secret_key, file_content, digestmod=hashlib.sha256)

        # Return the hexadecimal digest
        hex_digest = hmac_obj.hexdigest()
        print "HMAC-SHA256 Digest:", hex_digest
        return hex_digest

    except Exception as error:
        print "Error during HMAC computation:", error
        return None

# Example usage
item_description = "Example item"
file_content = "Hello, this is a test string!"  # Directly pass the content here
compute_hmac_sha256(item_description, file_content)
