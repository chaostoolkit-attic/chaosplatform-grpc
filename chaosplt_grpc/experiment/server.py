from typing import List

from grpc import Server

from .experiment_pb2_grpc import add_ExperimentServiceServicer_to_server, \
    ExperimentServiceServicer
from .message import GetRequest, GetReply, GetManyRequest, GetManyReply, \
    Experiment

__all__ = ["ExperimentService", "register_experiment_service"]


class ExperimentService(ExperimentServiceServicer):
    def Get(self, request: GetRequest, context) -> GetReply:
        experiment = self.get_organization(request.id, request.with_payload)
        return GetReply(experiment=experiment)

    def GetMany(self, request: GetManyRequest, context) -> GetManyReply:
        experiments = self.get_organizations(request.ids, request.with_payload)
        return GetManyReply(experiments=experiments)

    def get_experiment(self, experiment_id: str,
                       with_payload: bool = False) -> Experiment:
        raise NotImplementedError()

    def get_experiments(self, experiment_ids: List[str],
                        with_payload: bool = False) -> List[Experiment]:
        raise NotImplementedError()


def register_experiment_service(service: ExperimentService, server: Server):
    """
    Register an experiment service with the provided gRPC server.
    """
    add_ExperimentServiceServicer_to_server(service, server)
