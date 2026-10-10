import json
import boto3
import os
import urllib.parse
from io import BytesIO
from PIL import Image

s3_client = boto3.client('s3')
DEST_BUCKET = os.environ.get('DEST_BUCKET', 'retail-data-warehouse-destination-rakshit-1')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']  
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])    
        
        # Infinite loop protection guardrail
        if source_bucket == DEST_BUCKET:  
            print(f"Skipping {key}: Prevented recursive execution cycle.")  
            continue  
            
        # Ignore if the uploaded file is already inside a thumbnails folder
        if key.startswith('thumbnails/'):
            print(f"Skipping {key}: Already a thumbnail.")
            continue
        
        try:  
            # 1. Download image from Source S3 bucket
            print(f"Downloading {key} from {source_bucket}...") 
            response = s3_client.get_object(Bucket=source_bucket, Key=key) 
            image_content = response['Body'].read()  
        
            # 2. Process image using Pillow
            with Image.open(BytesIO(image_content)) as img:  
                if img.mode in ("RGBA", "P"):  
                    img = img.convert("RGB")  
                
                # Resize thumbnail (150x150)
                img.thumbnail((150, 150))  
            
                # 3. Save to memory buffer
                buffer = BytesIO()  
                img.save(buffer, 'JPEG', optimize=True, quality=85)  
                buffer.seek(0)  
            
            # Extract clean filename and define destination key path
            clean_filename = os.path.basename(key)
            name_without_ext = clean_filename.rsplit('.', 1)[0] if '.' in clean_filename else clean_filename
            new_key = f"thumbnails/thumbnail-{name_without_ext}.jpg"    
            
            # 4. Upload to Destination S3 Bucket (S3 automatically creates the 'thumbnails/' prefix path)
            print(f"Uploading {new_key} to {DEST_BUCKET}...")  
            s3_client.put_object(  
                Bucket=DEST_BUCKET,  
                Key=new_key,  
                Body=buffer,  
                ContentType='image/jpeg'  
            )  
            print(f"Successfully processed {key} and saved to {DEST_BUCKET}/{new_key}")    
            
        except Exception as e: 
            print(f"Error executing optimization on key {key}: {str(e)}") 
            raise e  
            
    return {  
        'statusCode': 200,  
        'body': json.dumps('Image execution pipeline finalized successfully.')  
    }  
