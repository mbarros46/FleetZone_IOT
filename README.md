
# 🛵 FleetZone - Gestão Inteligente de Pátios com Visão Computacional


## 🎯 Objetivo do Projeto
Automatizar o monitoramento e controle de motos no pátio da Mottu utilizando **Visão Computacional** com **Python**, **OpenCV** e **YOLOv8**, proporcionando eficiência, baixo custo e escalabilidade para múltiplas filiais.

---

## 🚨 Problema a Ser Resolvido
O controle manual de entrada e saída de motos nos pátios da Mottu é suscetível a erros, atrasos e falhas de rastreio. Faltam indicadores em tempo real que mostrem:
- Motos que sumiram ou foram deslocadas sem registro
- Veículos parados há muito tempo
- Tempo de inatividade de cada moto

---

## 💡 Nossa Solução
Uma plataforma simples e funcional que:
- Detecta e rastreia motos em tempo real usando câmeras comuns
- Gera alertas automáticos sobre movimentações suspeitas
- Registra histórico de presença para rastreabilidade
- Usa modelos leves e compatíveis com hardware simples

---

## 🛠️ Tecnologias Utilizadas
| Categoria | Ferramenta |
|----------|------------|
| Linguagem | Python 3.11+ |
| Visão Computacional | OpenCV, YOLOv8 (Ultralytics) |
| Execução | Desktop / Notebook com webcam ou vídeo |
| Simulação | Vídeo exemplo de pátio da Mottu |

---

## 🧪 Detecção de Motos
### 📌 Script 1 – OpenCV + MobileNet SSD
```bash
python detection/detect_motos_opencv.py
```

### 📌 Script 2 – YOLOv8
```bash
python detection/yolov8_detect.py
```
> Requer o modelo `yolov8n.pt` baixado no diretório raiz.

---

## ▶️ Execução Local
1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Execute qualquer um dos scripts acima.

---

## 📹 Link para o Pitch Técnico (YouTube)
🔗 [https://youtu.be/seu-video-aqui](https://youtu.be/seu-video-aqui) (modo não listado)

---

## 📁 Organização do Projeto
```
fleetzone/
├── detection/
│   ├── detect_motos_opencv.py
│   ├── yolov8_detect.py
│   ├── MobileNetSSD_deploy.prototxt
│   └── MobileNetSSD_deploy.caffemodel
├── assets/
│   └── sample_video.mp4
├── requirements.txt
├── README.md
└── video_pitch_link.txt
```

---

## 👥 Integrantes do Grupo
- Pedro Valendim Merise
- Miguel Barros Ramos
