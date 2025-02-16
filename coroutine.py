# Importar bibliotecas
import asyncio
import time


# Função asíncrona da primera atividade.
async def torrarPao():
    print("Inicia torra de pão --")
    await asyncio.sleep(4)
    print("finaliza torra de pao --")
    return "pão torrado"

# Função asíncrona da sungunda atividade.
async def fritarOvos():
    print("Inicia fritada de ovos --")
    await asyncio.sleep(2)
    print("finaliza fritada de ovos --")
    return "ovos prontos"

# Função asíncrona da terceira atividade.
async def enviarEmail(): 
    print("Inicio envio e-mail --")
    await asyncio.sleep(1)
    print("finaliza envio de e-mail --")
    return "e-mail enviado"


# Função asíncrona principal
async def main():

    """
    Este código criar uma rotina com programação ansíncrona em que se realizam tres chamadas
    ou funçãos. Cada uma dessas chamadas ou atividades têm tempos de execução diferentes. Ao
    usar programação asyncrona, garantimos que os processos sejam executados no momento em que
    outros estão tardando certo período de tempo. Usando este tipo de programação podemos ter
    várias funções sendo processadas ao mesmo tempo. Uma vantagem deste tipo de programação é
    que o tempo é reduzido, otimizando nosso desenvolvimento. Neste caso, o tempo total de
    execução foi de 4.02 segundos em vez de 7 segundos no caso síncrono.
    """

    tempo_inicio = time.time()

    # Saõ criadas diferentes tarefas para cada função
    # Isto permite a asincronia das mesmas
    tarefa_torrar = asyncio.create_task(torrarPao())
    tarefa_fritar = asyncio.create_task(fritarOvos())
    tarefa_enviar = asyncio.create_task(enviarEmail())

    # Crea-se um tempo de espera para cada atividade finaliar
    resultado_leitura = await tarefa_torrar
    resultado_email = await tarefa_fritar
    resultado_experimento = await tarefa_enviar

    tempo_final = time.time()
    time_diference = tempo_final - tempo_inicio

    print(f"estatus de leitura artigo: {resultado_leitura}")
    print(f"estadus de envio e-mail: {resultado_email}")
    print(f"estadus de experimento: {resultado_experimento}")

    print(f"tempo total de execução: {time_diference:.2f} segundos")

if __name__ == "__main__":
    asyncio.run(main())
