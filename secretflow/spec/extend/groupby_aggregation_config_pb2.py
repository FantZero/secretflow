# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/protos/secretflow/spec/extend/groupby_aggregation_config.proto

from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
)

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='secretflow/protos/secretflow/spec/extend/groupby_aggregation_config.proto',
    package='secretflow.spec.extend',
    syntax='proto3',
    serialized_options=b'\n\032org.secretflow.spec.extend',
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\nIsecretflow/protos/secretflow/spec/extend/groupby_aggregation_config.proto\x12\x16secretflow.spec.extend\"\xc8\x01\n\x0b\x43olumnQuery\x12I\n\x08\x66unction\x18\x01 \x01(\x0e\x32\x37.secretflow.spec.extend.ColumnQuery.AggregationFunction\x12\x13\n\x0b\x63olumn_name\x18\x02 \x01(\t\"Y\n\x13\x41ggregationFunction\x12\t\n\x05INVAL\x10\x00\x12\x07\n\x03SUM\x10\x01\x12\x08\n\x04MEAN\x10\x02\x12\x07\n\x03VAR\x10\x03\x12\x07\n\x03MIN\x10\x04\x12\x07\n\x03MAX\x10\x05\x12\t\n\x05\x43OUNT\x10\x06\"W\n\x18GroupbyAggregationConfig\x12;\n\x0e\x63olumn_queries\x18\x01 \x03(\x0b\x32#.secretflow.spec.extend.ColumnQueryB\x1c\n\x1aorg.secretflow.spec.extendb\x06proto3',
)


_COLUMNQUERY_AGGREGATIONFUNCTION = _descriptor.EnumDescriptor(
    name='AggregationFunction',
    full_name='secretflow.spec.extend.ColumnQuery.AggregationFunction',
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name='INVAL',
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='SUM',
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='MEAN',
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='VAR',
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='MIN',
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='MAX',
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name='COUNT',
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=213,
    serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_COLUMNQUERY_AGGREGATIONFUNCTION)


_COLUMNQUERY = _descriptor.Descriptor(
    name='ColumnQuery',
    full_name='secretflow.spec.extend.ColumnQuery',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='function',
            full_name='secretflow.spec.extend.ColumnQuery.function',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name='column_name',
            full_name='secretflow.spec.extend.ColumnQuery.column_name',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _COLUMNQUERY_AGGREGATIONFUNCTION,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=302,
)


_GROUPBYAGGREGATIONCONFIG = _descriptor.Descriptor(
    name='GroupbyAggregationConfig',
    full_name='secretflow.spec.extend.GroupbyAggregationConfig',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='column_queries',
            full_name='secretflow.spec.extend.GroupbyAggregationConfig.column_queries',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=304,
    serialized_end=391,
)

_COLUMNQUERY.fields_by_name['function'].enum_type = _COLUMNQUERY_AGGREGATIONFUNCTION
_COLUMNQUERY_AGGREGATIONFUNCTION.containing_type = _COLUMNQUERY
_GROUPBYAGGREGATIONCONFIG.fields_by_name['column_queries'].message_type = _COLUMNQUERY
DESCRIPTOR.message_types_by_name['ColumnQuery'] = _COLUMNQUERY
DESCRIPTOR.message_types_by_name['GroupbyAggregationConfig'] = _GROUPBYAGGREGATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColumnQuery = _reflection.GeneratedProtocolMessageType(
    'ColumnQuery',
    (_message.Message,),
    {
        'DESCRIPTOR': _COLUMNQUERY,
        '__module__': 'secretflow.protos.secretflow.spec.extend.groupby_aggregation_config_pb2'
        # @@protoc_insertion_point(class_scope:secretflow.spec.extend.ColumnQuery)
    },
)
_sym_db.RegisterMessage(ColumnQuery)

GroupbyAggregationConfig = _reflection.GeneratedProtocolMessageType(
    'GroupbyAggregationConfig',
    (_message.Message,),
    {
        'DESCRIPTOR': _GROUPBYAGGREGATIONCONFIG,
        '__module__': 'secretflow.protos.secretflow.spec.extend.groupby_aggregation_config_pb2'
        # @@protoc_insertion_point(class_scope:secretflow.spec.extend.GroupbyAggregationConfig)
    },
)
_sym_db.RegisterMessage(GroupbyAggregationConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)