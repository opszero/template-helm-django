# tiphyspy

Template App to deploy both a Flask app and a Jupyter Voila App

- Deploy a Flask Application
- Jupyter Voila WebApp
- [Example](https://tiphyspy.opszero.com/)

## Jupiter Voila

We deploy [Jupyter Notebooks](https://jupyter.org/) as
[Voila](https://github.com/voila-dashboards/voila) applications on Kubernetes.
This allows for the rapid creation of simple Webapps powered by Jupyter.

# Usage

## Dev

### Mac

```
pip3 install -r ./requirements.txt
voila
```

### Docker

```
docker buildx build --platform linux/amd64 -t opszero-voila-example .
docker run -p 8866:8866 -it opszero-voila-example
```

## Production

Deployed onto Kubernetes using an Ingress.

- [Check Github Actions for Deployment](https://github.com/opszero/tiphyspy/blob/main/.github/workflows/k8s.yml)
- [Tiphys for Deployment](https://github.com/opszero/tiphys)
  - [deploy.yaml](https://github.com/opszero/tiphyspy/blob/main/deploy.yaml)

# Pro Support

<a href="https://www.opszero.com"><img src="https://assets.opszero.com/images/opszero_11_29_2016.png" width="300px"/></a>

[opsZero provides support](https://www.opszero.com/devops) including:

- Kubernetes Deployment
- Implementation Guidance
- Security Posture
