# 🛵 FleetZone - Gestão Inteligente de Pátios com Visão Computacional

## 🎯 Objetivo do Projeto
Automatizar o monitoramento e controle de motos nos pátios da Mottu utilizando **Visão Computacional** com **Python**, **OpenCV** e **YOLOv8**, proporcionando eficiência, baixo custo e escalabilidade para múltiplas filiais.

---

## 🚨 Problema a Ser Resolvido
O controle manual de entrada e saída de motos nos pátios da Mottu é suscetível a erros, atrasos e falhas de rastreio. Atualmente, faltam indicadores em tempo real que informem:

- Motos que sumiram ou foram deslocadas sem registro
- Veículos parados há muito tempo
- Tempo de inatividade de cada moto

---

## 💡 Nossa Solução
Uma plataforma simples e funcional que:

- Detecta e rastreia motos em tempo real usando câmeras comuns (webcams ou vídeos)
- Gera alertas automáticos sobre movimentações suspeitas
- Registra histórico de presença para rastreabilidade
- Utiliza modelos leves e compatíveis com hardware simples e acessível

---

## 🛠️ Tecnologias Utilizadas

| Categoria           | Ferramenta                 |
|---------------------|---------------------------|
| Linguagem           | Python 3.11+              |
| Visão Computacional  | OpenCV, YOLOv8 (Ultralytics) |
| Execução            | Desktop / Notebook com webcam ou vídeo |
| Simulação           | Vídeo exemplo de pátio da Mottu |

---

## ⚙️ Requisitos do Ambiente

- Python 3.11 ou superior instalado
- Recomenda-se criar um ambiente virtual (virtualenv ou conda)
- Instalar as dependências via:
```bash
pip install -r requirements.txt
Requisitos principais:

opencv-python

ultralytics

numpy

filterpy

🧪 Detecção de Motos - Como Executar
1. OpenCV + MobileNet SSD (Modelo pré-treinado padrão)
Detecta motos usando modelo MobileNet SSD.

bash
Copiar
python detection/detect_motos_opencv.py --source assets/sample_video.mp4
--source aceita caminho de vídeo ou número da webcam (ex: 0)

Pode ser usado com webcam em tempo real

2. YOLOv8 (Ultralytics)
Detecta motos com maior precisão e capacidade de rastreamento.

bash
Copiar
python detection/yolov8_detect.py --source assets/sample_video.mp4
Necessário ter o modelo yolov8n.pt no diretório raiz

--source pode ser vídeo, webcam ou pasta de imagens

🔍 Sobre o Modelo YOLOv8
Modelo base yolov8n.pt (Nano) fornecido pela Ultralytics, leve e rápido

Pode ser customizado futuramente para melhorar detecção específica

O arquivo do modelo está incluso no projeto para facilitar o uso

▶️ Passo a Passo para Rodar Localmente
Clone ou baixe o projeto

Instale as dependências:

bash
Copiar
pip install -r requirements.txt
Baixe ou confirme que o arquivo yolov8n.pt está na raiz do projeto

Execute um dos scripts de detecção conforme explicado acima

📁 Estrutura do Projeto
Copiar
fleetzone/
├── detection/
│   ├── detect_motos_opencv.py
│   ├── yolov8_detect.py
│   ├── yolov8_tracking_sort.py
│   ├── MobileNetSSD_deploy.prototxt.txt
│   └── MobileNetSSD_deploy.caffemodel
├── assets/
│   └── sample_video.mp4
├── yolov8n.pt
├── requirements.txt
├── README.md
└── video_pitch_link.txt
📹 Pitch Técnico
🔗 Link para o pitch técnico no YouTube (modo não listado):
https://yout

👥 Integrantes do Grupo:

Pedro Valentim Merise Rm 556826

Miguel Barros Ramos Rm556652

📝 Licença
Este projeto está licenciado sob a licença MIT — veja o arquivo LICENSE para detalhes.

🚀 Próximos Passos / Roadmap
Melhorar detecção customizada para diferentes modelos e ângulos de motos

Implementar alertas via e-mail ou sistema de notificações

Adicionar interface web para visualização em tempo real e controle remoto

Otimizar processamento para execução em hardware embarcado (Raspberry Pi, Jetson Nano)
