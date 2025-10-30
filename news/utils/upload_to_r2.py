from os import environ
import boto3
from PIL import Image
from io import BytesIO

SECRET_ACCESS_KEY = '6dc9ec760fcc353173afd0fbd1816d617af87d39d3d1ea266d01a56a26fdb870'
ACCESS_KEY_ID = '1edb90b40249172b8fcc11709bd972e5'
ACCOUNT_ID='bef358e585ef9ba2ea76b368f4ce42f9'
ENDPOINT_URL=f"https://{ACCOUNT_ID}.r2.cloudflarestorage.com"



s3 = boto3.client(
        service_name='s3',
        endpoint_url=ENDPOINT_URL,
        aws_secret_access_key=SECRET_ACCESS_KEY,
        aws_access_key_id=ACCESS_KEY_ID
        )


def resize_and_upload(file_obj,key, bucket='updates247'):
    # 1. Open and resize the image
    content_type = key.split('/')[-1]
    content_type = f"image/{content_type}"
    if isinstance(file_obj, bytes):
        file_obj = BytesIO(file_obj)

    image = Image.open(file_obj)
    image = image.convert('RGB')  # in case it's RGBA or P
    image = image.resize((600, 300))

    # 2. Save the resized image to an in-memory buffer
    buffer = BytesIO()

    if 'JPEG' in str(key).upper():
        image.save(buffer, format='JPEG')
   #     filename += '.jpeg'

    elif 'JPG' in str(key).upper():
        image.save(buffer, format='JPEG')
   #     filename += '.jpg'

    elif 'PNG' in str(key).upper():
        image.save(buffer, format='PNG')
   #     filename += '.png'

    buffer.seek(0)
    key = f'news_photos/{key}'
    # 3. Upload to S3
    s3.upload_fileobj(buffer, bucket, key, ExtraArgs={'ContentType': f'{content_type}'})
    print('Image uploaded successfully')
    return f"{ENDPOINT_URL}/{key}"