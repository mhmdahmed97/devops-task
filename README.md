# Components of Task
- Deploy infrastructure using Terraform in the `infrastructure resources`
- Deploy colorization server 
- Deploy transcoding layer

## Steps to complete the task are provided below

### 1. AWS CLI configuration
- Open terminal and run the following command: `aws configure --profile <name-of-profile>`
- Follow the steps through by entering your `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

### 2. Deploy infrastructure
- Go to root directory of `infrastructure-resources`:
\`\`\`bash
cd infrastructure-resources
\`\`\`
- Open `providers.tf` and update AWS profile name.
- Run the following commands:
\`\`\`bash
terraform init
terraform plan
terraform apply
\`\`\`

### 3. Create and publish docker images
For the colorization-server:
- Go to the root directory of `server-resources`:
\`\`\`bash
cd server-resources
\`\`\`
- Login to your DockerHub repository using:
\`\`\`bash
docker login
\`\`\`
- Build, tag, and push the image:
\`\`\`bash
docker build -t colorization-server .
docker tag colorization-server:latest <your-docker-repo>/colorization-server:latest
docker push <your-docker-repo>/colorization-server:latest
\`\`\`

For the transcoder-server:
- Go to the root directory of `application-resources`:
\`\`\`bash
cd application-resources
\`\`\`
- Build, tag, and push the image:
\`\`\`bash
docker build -t transcoder-server .
docker tag transcoder-server:latest <your-docker-repo>/transcoder-server:latest
docker push <your-docker-repo>/transcoder-server:latest
\`\`\`

### 4. Installing Istio service-mesh
- First, install kubectl using your distribution's package manager. For Ubuntu and Debian based OS run:
\`\`\`bash
sudo apt update && sudo apt install kubectl
\`\`\`
- Connect to your AWS EKS cluster by running:
\`\`\`bash
aws eks update-kubeconfig --region <cluster-region> --name <cluster-name> --profile <profile-name>
\`\`\`
- Install istioctl on your host then run:
\`\`\`bash
istioctl install --set profile=demo -y
\`\`\`

### 5. Deploy the kubernetes manifests
For the colorization-server:
- Go to the root directory of `server-resources`:
\`\`\`bash
cd server-resources
\`\`\`
- Replace the image field with your image name .i.e `<your-docker-repo>/colorization-server:latest` in the `colorization-server.yaml` file.
- Deploy the colorization-server on the EKS cluster:
\`\`\`bash
kubectl apply -f colorization-server.yaml
\`\`\`

For the transcoder-server:
- Go to the root directory of `application-resources`:
\`\`\`bash
cd application-resources
\`\`\`
- Replace the image field with your image name .i.e `<your-docker-repo>/transcoder-server:latest` in the `transcoding-service.yaml` file.
- Deploy the transcoder-server on the EKS cluster:
\`\`\`bash
kubectl apply -f transcoding-service.yaml
\`\`\`

### 6. Testing the application setup
- Get the Load Balancer public IP for the transcoding-service:
\`\`\`bash
kubectl get svc -o wide
\`\`\`
- Using curl and the Load Balancer service IP received from the previous step, send a POST request with content-type as application/json with the content:
\`\`\`bash
curl -X POST -H "Content-Type: application/json" -d '{"op": "<operation>", "image": "<base64-encoded-image>"}' <Load Balancer IP>
\`\`\`

