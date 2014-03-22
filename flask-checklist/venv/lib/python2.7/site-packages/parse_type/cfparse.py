# -*- coding: utf-8 -*-
"""
Provides an extended :class:`parse.Parser` class that supports the
cardinality fields in (user-defined) types.
"""

from __future__ import absolute_import
from .cardinality_field import CardinalityField, CardinalityFieldTypeBuilder
from .parse_util import FieldParser
import parse
import logging


log = logging.getLogger(__name__)


class Parser(parse.Parser):
    """
    Provides an extended :class:`parse.Parser` with cardinality field support.
    A cardinality field is a type suffix for parse format expression, ala:

        "... {person:Person?} ..."   -- OPTIONAL: Cardinality zero or one, 0..1
        "... {persons:Person*} ..."  -- MANY0: Cardinality zero or more, 0..
        "... {persons:Person+} ..."  -- MANY:  Cardinality one  or more, 1..

    When the primary type converter for cardinality=1 is provided,
    the type variants for the other cardinality cases can be derived from it.

    This parser class automatically creates missing type variants for types
    with a cardinality field and passes the extended type dictionary
    to its base class.
    """
    # -- TYPE-BUILDER: For missing types in Fields with CardinalityField part.
    type_builder = CardinalityFieldTypeBuilder

    def __init__(self, schema, extra_types={}, type_builder=None):
        """
        Creates a parser with CardinalityField part support.

        :param schema:  Parse schema (or format) for parser (as string).
        :param extra_types:  Type dictionary with type converters.
        :param type_builder: Type builder to use for missing types.
        """
        missing = self.create_missing_types(schema, extra_types, type_builder)
        if missing:
            log.debug("MISSING TYPES: %s" % ",".join(missing.keys()))
            extra_types.update(missing)

        # -- FINALLY: Delegate to base class.
        super(Parser, self).__init__(schema, extra_types)

    @classmethod
    def create_missing_types(cls, schema, type_dict, type_builder=None):
        """
        Creates missing types for fields with a CardinalityField part.
        It is assumed that the primary type converter for cardinality=1
        is registered in the type dictionary.

        :param schema:  Parse schema (or format) for parser (as string).
        :param type_dict:  Type dictionary with type converters.
        :param type_builder: Type builder to use for missing types.
        :return: Type dictionary with missing types. Empty, if none.
        :raises: MissingTypeError,
                if a primary type converter with cardinality=1 is missing.
        """
        if not type_builder:
            type_builder = cls.type_builder

        missing = cls.extract_missing_special_type_names(schema, type_dict)
        return type_builder.create_type_variants(missing, type_dict)

    @staticmethod
    def extract_missing_special_type_names(schema, type_dict):
        """
        Extract the type names for fields with CardinalityField part.
        Selects only the missing type names that are not in the type dictionary.

        :param schema:     Parse schema to use (as string).
        :param type_dict:  Type dictionary with type converters.
        :return: Generator with missing type names (as string).
        """
        for name in FieldParser.extract_types(schema):
            if CardinalityField.matches_type(name) and (name not in type_dict):
                    yield name
