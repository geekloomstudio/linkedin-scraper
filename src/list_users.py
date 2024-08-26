import logging
import traceback

from helper import constants
from helper.decorators import sleep
from helper.request_handler import send_request
from profile_details import get_username
from services.mongodb.pymongo_client import upsert_document

responses = []

variables = "(\
    start:{0},\
    origin:FACETED_SEARCH,\
    query:(\
        keywords:{2},\
        flagshipSearchIntent:SEARCH_SRP,\
        queryParameters:List(\
            (\
                key:geoUrn,\
                value:List(103644278)\
            ),\
            (\
                key:network,\
                value:List({1})\
            ),\
            (\
                key:resultType,\
                value:List(PEOPLE)\
            )\
        ),\
        includeFiltersInResponse:false)\
    )&\
    queryId=voyagerSearchDashClusters.37920f17209f22c510dd410658abc540".replace(
    " ", ""
)


def upsert_user_profiles(data):
    """update or create new profile in mongodb

    Args:
        data (dict): {
            "included": [{}, {}, {}, ...]
        }
    """
    for included_data in data.get("included", []):
        if included_data.get("template") == constants.UNIVERSAL:
            # include username in the data to prevent duplicate entry
            username = get_username(included_data["navigationUrl"])
            included_data["username"] = username

            upsert_document(
                constants.MongodbCollections.PROFILES,
                {"username": username},
                data=included_data,
            )


@sleep(1, 3)
def list_user(offset, network, keywords):
    """returns list of users from linkedin api calling

    Args:
        offset (str): page number
        network (str):
            "F",  # 1st Connection
            "S",  # 2nd Connection
            "O",  # 3rd+ Connection
        keywords (str): "search keyword like ceo, bde, etc."

    Returns:
        tuple: status_code and json data
    """
    filled_variables = variables.format(offset, network, keywords)
    status_code, data = send_request(
        "get",
        f"https://www.linkedin.com/voyager/api/graphql?variables={filled_variables}",
    )
    if status_code == constants.status.HTTP_200_OK:
        return (status_code, data) if data["included"] else None

    return status_code, data


def main(keywords=None, network_list=None):
    """main function to execute the list user function with value setting."""
    users_list = []

    for network in network_list:
        try:
            print("➡ src/list_users.py:103 network:", network)

            for offset in range(
                constants.LinkedinPaginationConfig.START_PAGE,
                constants.LinkedinPaginationConfig.END_PAGE
                + constants.LinkedinPaginationConfig.PAGE_SIZE,
                constants.LinkedinPaginationConfig.PAGE_SIZE,
            ):
                print("➡ src/list_users.py:67 offset:", offset)

                status_code, users = list_user(offset, network, keywords)

                if status_code == constants.status.HTTP_200_OK and users:
                    users_list.append(users)
                else:
                    break

                upsert_user_profiles(users)

        except Exception:
            error = traceback.format_exc()
            logging.exception(error)


if __name__ == "__main__":
    main(
        keywords="cto",
        network_list=[
            # constants.LinkedinNetworkConfig.FIRST,
            # constants.LinkedinNetworkConfig.SECOND,
            constants.LinkedinNetworkConfig.THIRD,
        ],
    )

# 4d9e161cdf3cf64b1c9a7a7c1fc94cff
# aeba67850e106299f25de2eb3828c641
# 2ca312bdbe80fac72fd663a3e06a83e7
