# Projeto-consumindo-API-Twitter

Aplicação que faz o consumo da API do Twitter e arquiva os dados em uma banco MongoDB. Neste repositório há também um relatório no PowerBI que consome as informações do banco de dados

Informações relevantes para que o código e relatório consigam ser executados:

1 - Por questões de segurança as chaves da API Tweepy foram retiradas do código, para executá-lo é necessário o cadastro pela url https://apps.twitter.com

2 - Para a execução do código é necessário que tenha instalado na máquina o Docker Dektop. Para a instalação, seguir os passos na url https://docs.docker.com/desktop/windows/install/

3 - Como o MongoDB é um banco NoSQL e os dados desta aplicação são armazenados em arquivo JSON é necessária a instalação de conectores ODBC para que seja criado um schema que o PowerBI saiba ler.
