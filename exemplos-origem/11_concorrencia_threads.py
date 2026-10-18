import threading
import time
import random


class SistemaIngressos:

    def __init__(self, quantidade):
        self.ingressos = quantidade

        # Lock protege o recurso compartilhado
        self.lock = threading.Lock()

    def comprar(self, cliente, quantidade):

        # Simula o tempo de acesso ao sistema
        time.sleep(random.uniform(0.1, 0.5))

        # Região crítica
        with self.lock:

            if self.ingressos >= quantidade:
                self.ingressos -= quantidade

                print(
                    f"{cliente} comprou {quantidade} ingresso(s)."
                )

                print(
                    f"Restantes: {self.ingressos}"
                )

            else:
                print(
                    f"{cliente}: ingressos insuficientes."
                )


sistema = SistemaIngressos(10)

clientes = [
    ("Ana", 3),
    ("Bruno", 4),
    ("Carlos", 2),
    ("Daniela", 5),
    ("Eduardo", 2)
]

threads = []

print("=== VENDA DE INGRESSOS ===")

# Criação das threads
for nome, quantidade in clientes:

    thread = threading.Thread(
        target=sistema.comprar,
        args=(nome, quantidade)
    )

    threads.append(thread)

    thread.start()


# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()


print("\n=== RESULTADO FINAL ===")
print("Ingressos restantes:", sistema.ingressos)