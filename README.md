<img src="https://storage.googleapis.com/golden-wind/experts-club/capa-github.svg" />

# Coleta de métricas em cluster Kubernetes com Prometheus, Alertmanager e Grafana

Ao se utilizar um cluster Kubernetes é importante coletar as métricas de utilização para avaliar necessidade de expansão da infraestrutura, também para avaliar a saúde do ambiente.

O Prometheus é amplamente utilizado para coletar e armazenar essas métricas, o Alertmanager é a ferramenta para gerar alertas e informar os times corretos quando uma ação de correção é necessária e o Grafana é uma ótima ferramenta para visualização de dashboards do estado de "saúde" do ambiente.

Nesta aula veremos como fazer o deploy desses componentes e alguns exemplos de configuração para serem explorados conforme sua necessidade.

A implementação da aula foi feita em um cluster Kubernetes configurado em máquina física (cluster feito com o Raspberry Pi) mas pode ser feito na nuvem. No caso do cluster em máquina física, é preciso fazer o deploy do metallb, como está na aula porém na nuvem os provedores já entregam automaticamente essa funcionalidade, precisando somente fazer o deploy do Ingress Controller.
  - Metallb: https://metallb.universe.tf/
    - metallb-ns.yaml
    - metallb-configmap-single.yaml
    - metallb-deploy.yaml

  - Ingress Controller: https://kubernetes.github.io/ingress-nginx/
    - nginx-ingress-controller.yaml

  - Prometheus: https://prometheus.io/
    - prometheus-configmap.yaml
    - prometheus-rbac.yaml
    - prometheus-rules.yaml
    - prometheus-deploy.yaml

  - Alertmanager: https://prometheus.io/docs/alerting/latest/alertmanager/
    - alertmanager-configmap.yaml
    - alertmanager-template.yaml
    - alertmanager-deploy.yaml

  - Grafana: https://grafana.com/
    - grafana-datasource.yaml
    - grafana-deploy.yaml

  - Dashboards para o Grafana: https://grafana.com/grafana/dashboards/
    - grafana.json

  - Coletores para o Kubernetes:
    - metrics-server.yaml - https://github.com/kubernetes-sigs/metrics-server
    - kube-state-rbac.yaml
    - kube-state-deploy.yaml - https://github.com/kubernetes/kube-state-metrics

Para quem vai usar em cluster físico local e queira editar o arquivo "hosts" para configurar uma URL de acesso ao ambiente:
- no Windows, o arquivo hosts fica em: C:\Windows\System32\drivers\etc\
- no Linux (Ubuntu) o o arquivo hosts fica em: /etc/
- o arquivo hosts deve ser editado e acrescente no final do arquivo as linhas com as informações do seu ambiente, como exemplo:
  # inserir no final do arquivo a linha:
  192.168.15.240	www.demo.io  grafana.demo.io  prom.demo.io  alert.demo.io

Lembrando que o IP (no exemplo: 192.168.15.240 é o IP que você configurou no metallb-configmap-single.yaml e ***.demo.io é a URL que você quiser usar


## Sergio Siqueira

| [<img src="https://avatars.githubusercontent.com/u/5666390?v=4" width="75px;"/>](https://github.com/snsergio) |
| :-: |
|[Sergio Siqueira](https://github.com/snsergio)|

# metricas-kubernetes-prometheus-2022-02-28
Aplicar Prometheus, Alertmanager e Grafana em cluster Kubernetes
