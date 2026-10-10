
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="AWS Lambda Thumbnail Generator - Automatically generate 150x150 image thumbnails using Amazon S3, AWS Lambda, Python and Pillow.">
  <title>AWS Lambda Thumbnail Generator | Project Documentation</title>

  <style>
    :root {
      --bg: #0b1120;
      --panel: #111c30;
      --panel-light: #17243b;
      --text: #e5edf8;
      --muted: #9aabc4;
      --orange: #ff9900;
      --blue: #54a6ff;
      --border: #293850;
      --green: #43d9a3;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI",
                   Roboto, Arial, sans-serif;
      background:
        radial-gradient(ellipse at top right, #172747 0, transparent 42%),
        var(--bg);
      color: var(--text);
      line-height: 1.75;
    }

    a {
      color: var(--blue);
      text-decoration: none;
    }

    a:hover {
      color: var(--orange);
    }

    .container {
      width: min(1120px, 92%);
      margin: auto;
    }

    .topbar {
      padding: 18px 0;
      border-bottom: 1px solid var(--border);
      background: rgba(11, 17, 32, 0.85);
    }

    .topbar-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .brand {
      color: var(--text);
      font-weight: 800;
      font-size: 18px;
    }

    .brand span {
      color: var(--orange);
    }

    .top-link {
      font-size: 14px;
      font-weight: 600;
    }

    .hero {
      padding: 80px 0 62px;
      text-align: center;
    }

    .eyebrow {
      display: inline-block;
      border: 1px solid #674b1b;
      background: rgba(255, 153, 0, 0.09);
      color: #ffbd57;
      border-radius: 999px;
      padding: 5px 14px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1.3px;
      text-transform: uppercase;
      margin-bottom: 22px;
    }

    h1 {
      max-width: 900px;
      margin: auto;
      font-size: clamp(34px, 6vw, 64px);
      line-height: 1.1;
      letter-spacing: -2px;
    }

    h1 span {
      color: var(--orange);
    }

    .hero-description {
      color: var(--muted);
      max-width: 740px;
      margin: 24px auto;
      font-size: 17px;
    }

    .button-row {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 28px;
    }

    .button {
      display: inline-block;
      padding: 11px 20px;
      border-radius: 9px;
      font-weight: 750;
      border: 1px solid var(--border);
    }

    .button-primary {
      color: #151515;
      background: var(--orange);
      border-color: var(--orange);
    }

    .button-primary:hover {
      color: #151515;
      background: #ffb340;
    }

    .button-secondary {
      color: var(--text);
      background: var(--panel);
    }

    .tech-tags {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 9px;
      margin-top: 30px;
    }

    .tag {
      padding: 5px 11px;
      border: 1px solid var(--border);
      border-radius: 7px;
      background: var(--panel);
      color: #cbd7e8;
      font-size: 12px;
      font-weight: 650;
    }

    main {
      padding-bottom: 70px;
    }

    section {
      margin-top: 32px;
      padding: 30px;
      background: rgba(17, 28, 48, 0.88);
      border: 1px solid var(--border);
      border-radius: 16px;
    }

    .section-label {
      color: var(--orange);
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 1.7px;
      text-transform: uppercase;
      margin-bottom: 5px;
    }

    h2 {
      font-size: clamp(23px, 3vw, 32px);
      line-height: 1.25;
      margin-bottom: 16px;
    }

    h3 {
      font-size: 17px;
      margin-bottom: 8px;
    }

    p {
      color: #c4d0e0;
      margin-bottom: 12px;
    }

    ul, ol {
      padding-left: 23px;
      color: #c4d0e0;
      margin: 10px 0 15px;
    }

    li {
      margin: 6px 0;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 15px;
      margin-top: 22px;
    }

    .feature {
      padding: 20px;
      background: var(--panel-light);
      border: 1px solid var(--border);
      border-radius: 12px;
    }

    .feature-icon {
      font-size: 25px;
      margin-bottom: 10px;
    }

    .feature p {
      font-size: 14px;
      margin-bottom: 0;
    }

    .architecture {
      display: flex;
      justify-content: center;
      align-items: stretch;
      gap: 12px;
      flex-wrap: wrap;
      margin: 25px 0;
    }

    .architecture-node {
      min-width: 150px;
      flex: 1;
      text-align: center;
      padding: 18px 12px;
      border: 1px solid #344760;
      border-radius: 12px;
      background: var(--panel-light);
    }

    .architecture-node strong {
      display: block;
      color: var(--orange);
      margin: 7px 0;
    }

    .architecture-node small {
      color: var(--muted);
    }

    .arrow {
      display: flex;
      align-items: center;
      color: var(--orange);
      font-size: 24px;
      font-weight: 800;
    }

    .note {
      padding: 15px 17px;
      border-left: 3px solid var(--orange);
      background: rgba(255, 153, 0, 0.07);
      border-radius: 0 9px 9px 0;
      color: #d6dfeb;
      margin-top: 15px;
    }

    .code-block {
      overflow-x: auto;
      background: #080d17;
      border: 1px solid var(--border);
      padding: 16px;
      border-radius: 10px;
      color: #b9d5ff;
      font: 13px/1.7 Consolas, "Courier New", monospace;
      margin: 12px 0 18px;
      white-space: pre;
    }

    .screenshot-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 20px;
      margin-top: 22px;
    }

    .screenshot-card {
      overflow: hidden;
      background: #0a1323;
      border: 1px solid var(--border);
      border-radius: 12px;
    }

    .screenshot-card img {
      display: block;
      width: 100%;
      height: auto;
      min-height: 160px;
      object-fit: contain;
      background: #080d17;
    }

    .screenshot-info {
      padding: 15px;
    }

    .screenshot-info h3 {
      margin-bottom: 4px;
    }

    .screenshot-info p {
      font-size: 13px;
      margin: 0;
    }

    .step {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      margin: 20px 0;
    }

    .step-number {
      min-width: 34px;
      height: 34px;
      display: grid;
      place-items: center;
      border-radius: 9px;
      background: rgba(255, 153, 0, 0.13);
      border: 1px solid #674b1b;
      color: var(--orange);
      font-weight: 800;
    }

    .step-content p {
      margin-bottom: 0;
    }

    .table-wrap {
      overflow-x: auto;
      margin-top: 15px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      min-width: 480px;
    }

    th, td {
      text-align: left;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
    }

    th {
      color: var(--orange);
      background: var(--panel-light);
    }

    td {
      color: #c4d0e0;
    }

    code {
      color: #ffcb79;
      overflow-wrap: anywhere;
    }

    .status {
      display: inline-block;
      color: var(--green);
      border: 1px solid #245c4b;
      background: rgba(67, 217, 163, 0.08);
      border-radius: 6px;
      padding: 2px 8px;
      font-size: 12px;
      font-weight: 700;
    }

    footer {
      border-top: 1px solid var(--border);
      padding: 30px 0;
      text-align: center;
      color: var(--muted);
      font-size: 13px;
    }

    @media (max-width: 760px) {
      .hero {
        padding: 55px 0 40px;
      }

      section {
        padding: 21px;
      }

      .grid {
        grid-template-columns: 1fr;
      }

      .screenshot-grid {
        grid-template-columns: 1fr;
      }

      .arrow {
        transform: rotate(90deg);
        justify-content: center;
      }

      h1 {
        letter-spacing: -1px;
      }
    }

    @media print {
      body {
        background: #fff;
        color: #111;
      }

      section, .feature, .architecture-node, .screenshot-card {
        background: #fff;
        border-color: #ddd;
      }

      p, ul, ol, li, td, footer {
        color: #333;
      }

      .hero {
        padding-top: 30px;
      }

      a {
        color: #1256a0;
      }
    }
  </style>
</head>

<body>

  <header class="topbar">
    <div class="container topbar-inner">
      <a class="brand" href="#top">AWS <span>Thumbnail Generator</span></a>
      <a class="top-link"
         href="https://github.com/rakshitsinghh/aws-lambda-thumbnail-project"
         target="_blank" rel="noopener noreferrer">
        View GitHub Repository ↗
      </a>
    </div>
  </header>

  <div id="top" class="hero">
    <div class="container">
      <div class="eyebrow">Cloud Computing · Serverless Project</div>

      <h1>Automated Image <span>Thumbnail Generator</span></h1>

      <p class="hero-description">
        A serverless image-processing project using Amazon S3, AWS Lambda,
        Python and Pillow to generate 150 × 150 pixel thumbnails when images
        are uploaded to an S3 source bucket.
      </p>

      <div class="button-row">
        <a class="button button-primary"
           href="https://github.com/rakshitsinghh/aws-lambda-thumbnail-project"
           target="_blank" rel="noopener noreferrer">
          Explore Repository
        </a>

        <a class="button button-secondary" href="#screenshots">
          View Screenshots
        </a>
      </div>

      <div class="tech-tags">
        <span class="tag">AWS Lambda</span>
        <span class="tag">Amazon S3</span>
        <span class="tag">Python 3.12</span>
        <span class="tag">Pillow</span>
        <span class="tag">IAM</span>
        <span class="tag">CloudWatch</span>
      </div>
    </div>
  </div>

  <main class="container">

    <section id="overview">
      <div class="section-label">01 · Overview</div>
      <h2>Project Overview</h2>

      <p>
        The AWS Lambda Thumbnail Generator demonstrates event-driven,
        serverless image processing on Amazon Web Services. When an image
        is uploaded to a designated Amazon S3 source bucket, an S3 event
        can invoke an AWS Lambda function to process the image.
      </p>

      <p>
        The function uses Python and the Pillow image-processing library
        to create a smaller thumbnail and save the generated output in a
        separate destination bucket.
      </p>

      <div class="note">
        <strong>Important:</strong> This documentation describes the
        intended project workflow. Actual deployment status, successful
        executions and test results should be confirmed using the
        project's AWS console, logs and repository files.
      </div>
    </section>

    <section id="problem">
      <div class="section-label">02 · Problem Statement</div>
      <h2>Why Automate Thumbnail Generation?</h2>

      <p>
        Applications that handle uploaded images often need smaller
        versions for previews, galleries and image listings. Creating
        these versions manually can take time and does not scale well
        when many files are uploaded.
      </p>

      <div class="grid">
        <div class="feature">
          <div class="feature-icon">⚙️</div>
          <h3>Automation</h3>
          <p>Reduce repetitive manual image-processing work.</p>
        </div>

        <div class="feature">
          <div class="feature-icon">☁️</div>
          <h3>Serverless execution</h3>
          <p>Run image-processing code through a managed Lambda service.</p>
        </div>

        <div class="feature">
          <div class="feature-icon">🖼️</div>
          <h3>Consistent output</h3>
          <p>Generate thumbnails with a defined target size of 150 × 150.</p>
        </div>
      </div>
    </section>

    <section id="objectives">
      <div class="section-label">03 · Objectives</div>
      <h2>Project Objectives</h2>

      <ul>
        <li>Understand event-driven and serverless computing concepts.</li>
        <li>Use Amazon S3 to store original images and generated thumbnails.</li>
        <li>Configure an S3 object-created event to invoke Lambda.</li>
        <li>Process image files using Python and the Pillow library.</li>
        <li>Apply IAM permissions following the principle of least privilege.</li>
        <li>Use Amazon CloudWatch to inspect execution logs and errors.</li>
        <li>Keep source images and generated outputs in separate buckets.</li>
      </ul>
    </section>

    <section id="architecture">
      <div class="section-label">04 · Architecture</div>
      <h2>System Architecture</h2>

      <p>
        The following diagram illustrates the intended flow of the project.
      </p>

      <div class="architecture">
        <div class="architecture-node">
          <div>📤</div>
          <strong>Source S3 Bucket</strong>
          <small>Original image uploaded</small>
        </div>

        <div class="arrow">→</div>

        <div class="architecture-node">
          <div>⚡</div>
          <strong>S3 Event</strong>
          <small>Object-created notification</small>
        </div>

        <div class="arrow">→</div>

        <div class="architecture-node">
          <div>🐍</div>
          <strong>AWS Lambda</strong>
          <small>Python + Pillow processing</small>
        </div>

        <div class="arrow">→</div>

        <div class="architecture-node">
          <div>🖼️</div>
          <strong>Destination S3 Bucket</strong>
          <small>Generated thumbnail</small>
        </div>
      </div>

      <p>
        Amazon CloudWatch can be used to inspect Lambda execution logs.
        AWS Identity and Access Management (IAM) controls which resources
        the Lambda function can access.
      </p>

      <div class="note">
        The source and destination buckets should be separate. This helps
        prevent the Lambda function from repeatedly triggering itself
        when it writes a thumbnail.
      </div>
    </section>

    <section id="technologies">
      <div class="section-label">05 · Technology Stack</div>
      <h2>Tools and Services</h2>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Technology</th>
              <th>Purpose</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Amazon S3</td>
              <td>Stores source images and thumbnail output.</td>
            </tr>
            <tr>
              <td>AWS Lambda</td>
              <td>Runs the image-processing function.</td>
            </tr>
            <tr>
              <td>Python</td>
              <td>Implements the processing logic.</td>
            </tr>
            <tr>
              <td>Pillow</td>
              <td>Opens, resizes and saves image files.</td>
            </tr>
            <tr>
              <td>AWS IAM</td>
              <td>Defines execution permissions.</td>
            </tr>
            <tr>
              <td>Amazon CloudWatch</td>
              <td>Collects logs and helps troubleshoot execution.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <section id="configuration">
      <div class="section-label">06 · Configuration</div>
      <h2>Project Configuration</h2>

      <p>The project configuration described in this documentation is:</p>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Setting</th>
              <th>Configured or intended value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Source bucket</td>
              <td><code>my-project-images-source</code></td>
            </tr>
            <tr>
              <td>Destination bucket</td>
              <td><code>my-project-images-destination</code></td>
            </tr>
            <tr>
              <td>IAM execution role</td>
              <td><code>LambdaImageProcessorRole</code></td>
            </tr>
            <tr>
              <td>Inline IAM policy</td>
              <td><code>LambdaImageProcessingPolicy</code></td>
            </tr>
            <tr>
              <td>Runtime</td>
              <td>Python 3.12, if selected in the deployment</td>
            </tr>
            <tr>
              <td>Thumbnail dimensions</td>
              <td>150 × 150 pixels</td>
            </tr>
            <tr>
              <td>Supported image formats</td>
              <td>JPEG and PNG input, subject to implementation</td>
            </tr>
            <tr>
              <td>Output format</td>
              <td>JPEG, subject to implementation</td>
            </tr>
            <tr>
              <td>Event</td>
              <td><code>s3:ObjectCreated:*</code></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="note">
        Confirm these names against your AWS account. Bucket names are
        globally unique, so your actual bucket names may differ.
      </div>
    </section>

    <section id="implementation">
      <div class="section-label">07 · Implementation</div>
      <h2>How the Workflow Operates</h2>

      <div class="step">
        <div class="step-number">1</div>
        <div class="step-content">
          <h3>Upload an image</h3>
          <p>An original image is uploaded to the source S3 bucket.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-number">2</div>
        <div class="step-content">
          <h3>Trigger the Lambda function</h3>
          <p>An eligible object-created event invokes the configured function.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-number">3</div>
        <div class="step-content">
          <h3>Read and process the image</h3>
          <p>The function retrieves the source image and uses Pillow to resize it.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-number">4</div>
        <div class="step-content">
          <h3>Save the thumbnail</h3>
          <p>The generated thumbnail is written to the destination bucket.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-number">5</div>
        <div class="step-content">
          <h3>Review logs</h3>
          <p>CloudWatch logs can help verify execution and identify errors.</p>
        </div>
      </div>

      <h3>Example processing logic</h3>
      <p>
        The following is an illustrative Pillow example, not a claim that
        it exactly matches the deployed Lambda function. The actual handler
        should also retrieve the S3 object and upload the result.
      </p>

      <div class="code-block">from PIL import Image

def create_thumbnail(image, size=(150, 150)):
    """Create a thumbnail while preserving image proportions."""
    image.thumbnail(size)
    return image</div>

      <p>
        Pillow must be available to the Lambda runtime through a compatible
        deployment package or Lambda layer. Check the implementation in
        your repository for the actual handler and dependency setup.
      </p>
    </section>

    <section id="screenshots">
      <div class="section-label">08 · Visual Documentation</div>
      <h2>AWS Project Screenshots</h2>

      <p>
        The screenshots below reference the image files in the root of the
        GitHub repository. Each image is displayed at its natural aspect
        ratio to avoid unnecessary cropping.
      </p>

      <div class="screenshot-grid">

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113529.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113529.png"
              alt="AWS Lambda thumbnail project screenshot 1"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 01</h3>
            <p>AWS project console view.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113545.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113545.png"
              alt="AWS Lambda thumbnail project screenshot 2"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 02</h3>
            <p>Project configuration evidence.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113613.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113613.png"
              alt="AWS Lambda thumbnail project screenshot 3"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 03</h3>
            <p>Image-processing workflow evidence.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113629.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113629.png"
              alt="AWS Lambda thumbnail project screenshot 4"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 04</h3>
            <p>Additional AWS configuration evidence.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113649.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113649.png"
              alt="AWS Lambda thumbnail project screenshot 5"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 05</h3>
            <p>Additional project evidence.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113718.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113718.png"
              alt="AWS Lambda thumbnail project screenshot 6"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 06</h3>
            <p>Additional project evidence.</p>
          </div>
        </article>

        <article class="screenshot-card">
          <a href="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113739.png"
             target="_blank" rel="noopener noreferrer">
            <img
              src="https://raw.githubusercontent.com/rakshitsinghh/aws-lambda-thumbnail-project/main/Screenshot%202026-10-10%20113739.png"
              alt="AWS Lambda thumbnail project screenshot 7"
              loading="lazy">
          </a>
          <div class="screenshot-info">
            <h3>Screenshot 07</h3>
            <p>Additional project evidence.</p>
          </div>
        </article>

      </div>

      <div class="note">
        If an image does not load, check that its filename and capitalization
        exactly match the repository. GitHub filenames are case-sensitive.
      </div>
    </section>

    <section id="testing">
      <div class="section-label">09 · Testing</div>
      <h2>Testing and Verification Checklist</h2>

      <p>
        Use this checklist to document the actual results from your AWS
        environment. Mark each item complete only after verifying it.
      </p>

      <ul>
        <li>Confirm the source and destination S3 buckets exist.</li>
        <li>Confirm the Lambda function uses the expected runtime and handler.</li>
        <li>Confirm Pillow imports successfully in Lambda.</li>
        <li>Verify the S3 event notification and any file suffix filters.</li>
        <li>Upload a test image and check whether Lambda is invoked.</li>
        <li>Check that a thumbnail appears in the destination bucket.</li>
        <li>Verify the output image dimensions and file format.</li>
        <li>Review CloudWatch logs for errors or execution details.</li>
        <li>Test invalid or unsupported files if the implementation handles them.</li>
      </ul>

      <div class="note">
        Do not report a test as successful unless you have confirmed the
        corresponding output or log evidence.
      </div>
    </section>

    <section id="security">
      <div class="section-label">10 · Security</div>
      <h2>Security Considerations</h2>

      <ul>
        <li>Grant Lambda only the S3 read and write permissions it requires.</li>
        <li>Restrict permissions to the intended source and destination buckets.</li>
        <li>Use the Lambda execution role instead of embedding AWS credentials.</li>
        <li>Keep source and output buckets separate to avoid recursive invocations.</li>
        <li>Validate file types and handle image-processing exceptions.</li>
        <li>Review CloudWatch logs without exposing sensitive data.</li>
        <li>Never commit access keys, secret keys or other credentials to GitHub.</li>
      </ul>
    </section>

    <section id="future">
      <div class="section-label">11 · Future Enhancements</div>
      <h2>Future Scope</h2>

      <div class="grid">
        <div class="feature">
          <div class="feature-icon">📐</div>
          <h3>Multiple sizes</h3>
          <p>Generate thumbnail presets for different applications.</p>
        </div>

        <div class="feature">
          <div class="feature-icon">🛡️</div>
          <h3>Validation</h3>
          <p>Improve validation, exception handling and failure reporting.</p>
        </div>

        <div class="feature">
          <div class="feature-icon">📊</div>
          <h3>Monitoring</h3>
          <p>Add metrics, alarms and operational dashboards.</p>
        </div>
      </div>
    </section>

    <section id="learning">
      <div class="section-label">12 · Learning Outcomes</div>
      <h2>What This Project Demonstrates</h2>

      <ul>
        <li>Understanding of AWS serverless architecture.</li>
        <li>Object storage and event notifications using Amazon S3.</li>
        <li>Python-based image processing with Pillow.</li>
        <li>IAM role and permission concepts.</li>
        <li>CloudWatch logging and troubleshooting fundamentals.</li>
        <li>Separation of source data and generated outputs.</li>
      </ul>
    </section>

    <section id="author">
      <div class="section-label">13 · Project Information</div>
      <h2>Project Details</h2>

      <div class="table-wrap">
        <table>
          <tbody>
            <tr>
              <th>Project Title</th>
              <td>AWS Lambda Automated Thumbnail Generator</td>
            </tr>
            <tr>
              <th>Student</th>
              <td>Rakshit Singh</td>
            </tr>
            <tr>
              <th>Roll Number</th>
              <td>23eacad094</td>
            </tr>
            <tr>
              <th>Branch</th>
              <td>B.Tech — Artificial Intelligence &amp; Data Science</td>
            </tr>
            <tr>
              <th>Organization</th>
              <td>GRRAS Solutions Pvt. Ltd.</td>
            </tr>
            <tr>
              <th>Repository</th>
              <td>
                <a href="https://github.com/rakshitsinghh/aws-lambda-thumbnail-project"
                   target="_blank" rel="noopener noreferrer">
                  aws-lambda-thumbnail-project
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <section id="references">
      <div class="section-label">14 · References</div>
      <h2>Official Documentation</h2>

      <ul>
        <li>
          <a href="https://docs.aws.amazon.com/lambda/"
             target="_blank" rel="noopener noreferrer">
            AWS Lambda Documentation
          </a>
        </li>
        <li>
          <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/"
             target="_blank" rel="noopener noreferrer">
            Amazon S3 User Guide
          </a>
        </li>
        <li>
          <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/"
             target="_blank" rel="noopener noreferrer">
            AWS Identity and Access Management
          </a>
        </li>
        <li>
          <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/"
             target="_blank" rel="noopener noreferrer">
            Amazon CloudWatch Documentation
          </a>
        </li>
        <li>
          <a href="https://pillow.readthedocs.io/"
             target="_blank" rel="noopener noreferrer">
            Pillow Documentation
          </a>
        </li>
      </ul>
    </section>

  </main>

  <footer>
    <div class="container">
      <p>
        AWS Lambda Thumbnail Generator · Project documentation by Rakshit Singh
      </p>
      <p>
        <a href="https://github.com/rakshitsinghh/aws-lambda-thumbnail-project"
           target="_blank" rel="noopener noreferrer">
          GitHub Repository
        </a>
      </p>
    </div>
  </footer>

</body>
</html>
