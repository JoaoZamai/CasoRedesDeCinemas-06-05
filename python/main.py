from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController
from view.sessao_view import SessaoView

def main():
    repository = SessaoRepository()
    service = SessaoService(repository)
    controller = SessaoController(service)
    view = SessaoView(controller)

    view.solicita_consulta()


if __name__ == "__main__":
    main()