import cv2

def abrir_camera():
    # Inicializa a captura de vídeo. O número 0 representa a câmera padrão do PC.
    # (Se você tiver uma webcam USB extra, pode tentar usar 1 ou 2)
    camera = cv2.VideoCapture(0)

    # Verifica se o Python conseguiu acesso à câmera
    if not camera.isOpened():
        print("Erro: Não foi possível acessar a câmera. Verifique as permissões.")
        return

    print("Câmera ativada! Pressione a tecla 'q' na janela do vídeo para fechar.")

    # Loop contínuo para ler quadro a quadro (frame)
    while True:
        # Lendo o frame atual da câmera
        sucesso, frame = camera.read()

        # Se falhar em capturar o frame, interrompe o loop
        if not sucesso:
            print("Erro ao capturar a imagem da câmera.")
            break

        # Exibe o frame capturado em uma janela GUI chamada "Minha Câmera"
        cv2.imshow("Minha Câmera", frame)

        # Aguarda 1 milissegundo para ver se alguma tecla foi pressionada.
        # Se a tecla 'q' for pressionada, quebra o loop e fecha.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Após quebrar o loop, libera a câmera e destrói as janelas GUI
    camera.release()
    cv2.destroyAllWindows()

# Executa o código
if __name__ == "__main__":
    abrir_camera()