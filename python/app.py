from repository.sessao_repository import SessaoRepository
from service.sessao_service import SessaoService
from controller.sessao_controller import SessaoController
from view.sessao_view_web import SessaoViewWeb


def main():
    repository = SessaoRepository()
    service = SessaoService(repository)
    controller = SessaoController(service)
    view_web = SessaoViewWeb(controller)

    view_web.run()


if __name__ == "__main__":
    main()