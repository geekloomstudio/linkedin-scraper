"""Mongo db driver and utility functions."""

import collections
import logging
import os

from bson.objectid import ObjectId
from pymongo import ASCENDING, DESCENDING, MongoClient

import config  # noqa
from helper import constants

MONGO = None
TIMEOUT = 10000
EXPIRE_TIME = 14400  # 4 hours
DB_CONNECTION = {}


def mongoconnection(to=TIMEOUT):
    """Global connection handle for mongo"""
    global MONGO
    if MONGO:
        return MONGO
    dburl = os.getenv("db_host")
    logging.info("dburl: %s", repr(dburl))
    username = os.getenv("db_username", default=None)
    logging.info("username: %s", repr(username))
    password = os.getenv("db_password", default=None)
    logging.info("password: %s", repr(password))
    if username and password:
        MONGO = MongoClient(
            host=dburl,
            serverSelectionTimeoutMS=to,
            username=username,
            password=password,
        )

    else:
        logging.info("dburl: %s", repr(dburl))
        MONGO = MongoClient(
            host=dburl,
            serverSelectionTimeoutMS=to,
        )
    return MONGO


def mongodb(dbname=None):
    """Get the dbhandle for the database, if none then default database, 'test'"""
    global DB_CONNECTION
    if not dbname:
        dbname = os.getenv("db_name")
        logging.info("dbname: %s", repr(dbname))

    if dbname not in DB_CONNECTION:
        dbconnection = mongoconnection()
        db = dbconnection[dbname]
        DB_CONNECTION[dbname] = db

    return DB_CONNECTION[dbname]


def get_database_name():
    dbname = os.getenv("db_name")
    return dbname


def get_collection(dbname, collection):
    """Get the collection new or existing."""
    coll = None
    db = mongodb(dbname)
    if db and collection:
        coll = db[collection]
    return coll


def collection_names(dbname):
    """Find all the collections in the databases."""
    db = mongodb(dbname)
    # colls = db.collection_names(include_system_collections=False)
    colls = db.list_collection_names()
    return colls


def find_and_update_document(
    collection,
    query={},
    data={},
    unset_data={},
    push_data={},
    specific_field_update=False,
):
    """find and update single document into the collection."""
    db = mongodb(get_database_name())
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        if specific_field_update is False:
            collection.update_many(
                query, {"$set": data, "$unset": unset_data, "$push": push_data}
            )
        else:
            collection.update_one(
                query, {"$set": data, "$unset": unset_data, "$push": push_data}
            )
        return True
    return False


def find_documents(
    collection,
    query={},
    projection=None,
    aggregate=None,
    sort=None,
    limit=None,
    skip=None,
    distinct=None,
):
    """Find the documents based on the query"""
    docs = []
    db = mongodb(get_database_name())

    collection = db[collection] if db is not None and collection else None
    if collection is not None:

        if aggregate:
            results = collection.aggregate(aggregate)
        elif distinct:
            results = collection.distinct(distinct, query)
        else:
            if projection:
                results = collection.find(filter=query, projection=projection)
            else:
                results = collection.find(filter=query)
        if sort:
            results = results.sort(*sort)
        if limit:
            results = results.limit(limit)
        if skip:
            results = results.skip(skip)

        for result in results:
            result["_id"] = str(result["_id"])
            docs.append(result)
    return docs


def sort_dict(data):
    vals = []
    for key, val in data.items():
        if isinstance(val, dict):
            sub_dict = sort_dict(val)
            vals.append((key, sub_dict))
        else:
            vals.append((key, val))
    sorted_vals = sorted(vals, key=lambda x: x[0])
    return collections.OrderedDict(sorted_vals)


def insert_document(collection, data={}, check_keys=True):
    """insert one document into the collection."""
    db = mongodb(get_database_name())
    collection = db[collection] if db is not None and collection else None
    doc_id_str = None
    if collection is not None:
        if check_keys:
            doc_id = collection.insert_one(data).inserted_id
        else:
            doc_id = collection.insert(data, check_keys=False)
        doc_id_str = str(doc_id) if doc_id else None
    return doc_id_str


def upsert_document(
    collection,
    query={},
    projection=None,
    aggregate=None,
    sort=None,
    limit=None,
    skip=None,
    distinct=None,
    data={},
    unset_data={},
    push_data={},
    specific_field_update=False,
):
    docs = find_documents(
        collection,
        query,
        projection,
        aggregate,
        sort,
        limit,
        skip,
        distinct,
    )
    if not docs:
        insert_document(collection, data)
    else:
        find_and_update_document(
            collection, query, data, unset_data, push_data, specific_field_update
        )

    docs = find_documents(
        collection,
        query,
        projection,
        aggregate,
        sort,
        limit,
        skip,
        distinct,
    )

    return docs


def delete_documents(collection, query, dbname):
    """Delete the document based on the query"""
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        collection.delete_many(query)
        return True
    return False


def check_document(collection, docid, dbname=None):
    """Find the document based on the docid"""
    doc = None
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        obj_id = docid if isinstance(docid, ObjectId) else ObjectId(docid)
        doc = collection.find_one({"_id": obj_id})
    return doc


def count_documents(collection, query={}, dbname=None):
    """Count the documents based on the query"""
    count = None
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        query = {} if query is None else query
        count = collection.count_documents(query)
    return count


def distinct_documents(collection, field=None, dbname=None):
    """Count the documents based on the query"""
    count = []
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection and field:
        count = collection.distinct(field)
    return count


def create_indexes(collection, dbname, fields):
    """The fields to be indexed"""
    result = None
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        # index_fields = [(field, ASCENDING) for field in fields]
        result = collection.create_index(fields, unique=True)
    return result


def get_collection_size(collection_name):
    db_name = os.getenv("db_name")
    collection = get_collection(db_name, collection_name)
    return collection.count()


def index_information(collection, dbname):
    """index information of the collection"""
    index_info = None
    db = mongodb(dbname)
    collection = db[collection] if db is not None and collection else None
    if collection is not None:
        index_info = sorted(list(collection.index_information()))
    return index_info


def sort_field(name, asc=True):
    return (name, ASCENDING if asc else DESCENDING)


if __name__ == "__main__":
    db = find_documents(constants.MongodbCollections.PROFILES, {})
    print("➡ src/services/mongodb/pymongo_client.py:279 db:", db)
    logging.info("db: %s", repr(db))
