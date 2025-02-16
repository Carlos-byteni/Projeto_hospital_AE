# Importar biblioteca
import time

# Função torar pão.
def torrarPao():
    print("-- Inicia torra de pão --")
    time.sleep(4)
    print("-- finaliza torra de pao --")
    return "pão torrado"

# Função fritar ovos.
def fritarOvos():
    print("-- Inicia fritada de ovos --")
    time.sleep(2)
    print("-- finaliza fritada de ovos --")
    return "ovos prontos"

# Função que chama enviar e-mail.
def enviarEmail():
    print("-- Inicio envio e-mail --")
    time.sleep(1)
    print("-- finaliza envio de e-mail --")
    return "e-mail enviado"

# Função principal que visualiza el processo síncrono de cada atividade.
def main():

    """
    Este código criar uma rotina com programação síncrona em que se realizam tres chamadas
    ou funçãos. Este tipo de rotina chama cada função(proceso) de forma que espera finalizar cada uma
    para a seguinte ser chamada. Neste exercício, as três chamadas ocorrem em um tempo total de 7 segundos.
    """

    tempo_inicio = time.time()

    resultado_torrar = torrarPao()
    result_fritar = fritarOvos()
    resultado_enviar = enviarEmail()

    tempo_final = time.time()
    time_diference = tempo_final - tempo_inicio

    print(f"estatus de torrar pão: {resultado_torrar}")
    print(f"estadus de fritar ovos: {result_fritar}")
    print(f"estadus de enviar e-mail: {resultado_enviar}")
    print(f"tempo total de execução: {time_diference:.2f} segundos")

if __name__ == "__main__":
    main()
