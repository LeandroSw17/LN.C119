import cv2
import math

p1 = 530
p2 = 300

xs = []
ys = []

def goal_track(img, bbox):
    x, y, w, h = [int(val) for val in bbox]
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img, (c1, c2), 2, (0, 0, 255), 5)

    cv2.circle(img, (int(p1), int(p2)), 2, (0, 255, 0), 3)
    dist = math.sqrt(((c1 - p1)**2) + (c2 - p2)**2)
    print(dist)

    if dist <= 20:
        cv2.putText(img, "Ponto", (300, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs) - 1):
        cv2.circle(img, (xs[i], ys[i]), 2, (0, 0, 255), 5)

def drawBox(img, bbox):
    x, y, w, h = [int(val) for val in bbox]
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, "Rastreando", (75, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def main():
    video_path = 'C:/Users/Leandro Oliveira/Desktop/PRO_1-4_C119_TemplateDoProjeto-main/footvolleyball.mp4'  # Insira o caminho para o vídeo

    # Inicialização do rastreador (usando o rastreador MIL)
    tracker = cv2.TrackerMIL_create()

    # Lê o vídeo
    cap = cv2.VideoCapture(video_path)

    ret, img = cap.read()

    # Selecione a caixa delimitadora na imagem
    bbox = cv2.selectROI("tracking", img, False)

    # Inicialize o rastreador em img e na caixa delimitadora
    tracker.init(img, bbox)

    while True:
        ret, img = cap.read()

        if not ret:
            break

        success, bbox = tracker.update(img)

        if success:
            drawBox(img, bbox)
            goal_track(img, bbox)
        else:
            cv2.putText(img, "Errou", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Tracking", img)
        if cv2.waitKey(1) == 27:  # Pressione Esc para sair
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
