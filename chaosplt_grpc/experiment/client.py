from typing import List

from grpc import Channel

from .experiment_pb2_grpc import ExperimentServiceStub
from .message import Experiment, GetRequest, GetManyRequest

__all__ = ["get_experiment", "get_experiments"]


def get_experiment(channel: Channel, experiment_id: str,
                   with_payload: bool = False) -> Experiment:
    """
    Get an organization
    """
    stub = ExperimentServiceStub(channel)
    response = stub.Get(
        GetRequest(id=experiment_id, with_payload=with_payload))
    return response.workspace


def get_experiments(channel: Channel, experiment_ids: List[str],
                    with_payload: bool = False) -> List[Experiment]:
    """
    Get many organizations
    """
    stub = ExperimentServiceStub(channel)
    response = stub.GetMany(
        GetManyRequest(ids=experiment_ids, with_payload=with_payload))
    return response.workspaces
