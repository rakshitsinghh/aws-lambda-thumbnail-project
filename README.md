
# AWS Lambda Automated Image Thumbnail Generator

An event-driven serverless project that automatically generates **150 × 150 pixel thumbnails** whenever an image is uploaded to Amazon S3.

## Key Features

- **Automatic Processing:** S3 upload events trigger AWS Lambda.
- **Thumbnail Generation:** Python and Pillow resize images to 150 × 150 pixels.
- **Serverless Architecture:** No server management required.
- **Separate Storage:** Original and thumbnail images are stored in different S3 buckets.
- **Monitoring:** AWS CloudWatch records execution logs and errors.
- **Secure Access:** IAM roles and permissions control AWS resource access.

## Project Flow

```text
Upload Image to Source S3
          ↓
     S3 Event Trigger
          ↓
    AWS Lambda Function
          ↓
    Pillow Image Processing
          ↓
   Resize to 150 × 150
          ↓
Save Thumbnail to Destination S3
          ↓
   CloudWatch Logs
```

## Technologies Used

- **AWS:** Lambda, S3, IAM, CloudWatch
- **Language:** Python 3.12
- **Library:** Pillow
- **Trigger:** Amazon S3 ObjectCreated event

## AWS Configuration

| Component | Name / Configuration |
|---|---|
| Source Bucket | `my-project-images-source` |
| Destination Bucket | `my-project-images-destination` |
| Lambda Function Role | `LambdaImageProcessorRole` |
| IAM Policy | `LambdaImageProcessingPolicy` |
| Thumbnail Size | `150 × 150 pixels` |
| Supported Formats | JPG, PNG |

## Screenshots

### 1. AWS Lambda Configuration
![Lambda Configuration](Screenshot%202026-10-10%20113545.png)

### 2. S3 Bucket Setup
![S3 Setup](Screenshot%202026-10-10%20113613.png)

### 3. Event Trigger Configuration
![S3 Trigger](Screenshot%202026-10-10%20113629.png)

### 4. Image Processing
![Image Processing](Screenshot%202026-10-10%20113649.png)

### 5. Output Verification
![Output Verification](Screenshot%202026-10-10%20113718.png)

### 6. CloudWatch Logs
![CloudWatch Logs](Screenshot%202026-10-10%20113739.png)

## Expected Outcome

Uploading a supported image to the source bucket triggers Lambda processing, generates a thumbnail, and stores the output in the destination bucket. CloudWatch can be used to inspect execution logs.

## Learning Outcomes

- Serverless application development
- AWS S3 event notifications
- Lambda function deployment
- IAM permissions and security
- Image processing with Python
- Cloud monitoring and debugging

## Author

**Rakshit Singh**  
B.Tech — Artificial Intelligence & Data Science  
Roll Number: `23eacad094`  
Organization: GRRAS Solutions Pvt. Ltd.

## References

- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
