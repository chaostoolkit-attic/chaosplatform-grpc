#!/bin/bash
set -eo pipefail

function generate () {
    echo "Generating gRPC stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        auth/auth.proto
    sed -i "s/from auth/from ./g" \
        chaosplt_grpc/auth/auth_pb2_grpc.py
    echo "Generated auth stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        organization/organization.proto
    sed -i "s/from organization/from ./g" \
        chaosplt_grpc/organization/organization_pb2_grpc.py
    echo "Generated organization stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        scheduler/scheduler.proto
    sed -i "s/from scheduler/from ./g" \
        chaosplt_grpc/scheduler/scheduler_pb2_grpc.py
    echo "Generated scheduler stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        user/user.proto
    sed -i "s/from user/from ./g" \
        chaosplt_grpc/user/user_pb2_grpc.py
    echo "Generated user stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        workspace/workspace.proto
    sed -i "s/from workspace/from ./g" \
        chaosplt_grpc/workspace/workspace_pb2_grpc.py
    echo "Generated workspace stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        activity/activity.proto
    sed -i "s/from activity/from ./g" \
        chaosplt_grpc/activity/activity_pb2_grpc.py
    echo "Generated activity stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        experiment/experiment.proto
    sed -i "s/from experiment/from ./g" \
        chaosplt_grpc/experiment/experiment_pb2_grpc.py
    sed -i "s/from execution/from chaosplt_grpc.execution/g" \
        chaosplt_grpc/experiment/experiment_pb2.py
    echo "Generated experiment stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        execution/execution.proto
    sed -i "s/from execution/from ./g" \
        chaosplt_grpc/execution/execution_pb2_grpc.py
    echo "Generated execution stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        registration/registration.proto
    sed -i "s/from registration/from ./g" \
        chaosplt_grpc/registration/registration_pb2_grpc.py
    echo "Generated registration stubs"

    python -m grpc_tools.protoc \
        -I protos \
        --python_out=chaosplt_grpc \
        --grpc_python_out=chaosplt_grpc \
        scheduling/scheduling.proto
    sed -i "s/from scheduling/from ./g" \
        chaosplt_grpc/scheduling/scheduling_pb2_grpc.py
    echo "Generated scheduling stubs"
}

function main () {
    generate || return 1
}

main "$@" || exit 1
exit 0