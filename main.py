from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedidoUseCase
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.presenters.pedido_presenter import PedidoPresenter

def main():
    repository = MemoryPedidoRepository()
    use_case = CriarPedidoUseCase(repository)
    presenter = PedidoPresenter()
    controller = PedidoController(use_case, presenter)

    print("--- Sistema de Pedidos Inicializado ---")
    
    pedido_data = {
        "cliente": "Engenheiro(a) de Software",
        "valor_original": 100.0
    }

    resultado = controller.criar(pedido_data)
    print(resultado)

if __name__ == "__main__":
    main()