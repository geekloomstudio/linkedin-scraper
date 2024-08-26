import re

from helper import constants
from helper.request_handler import send_request
from services.mongodb.pymongo_client import find_documents, upsert_document

variables = "(\
    vanityName:{0}\
    )&\
    queryId=voyagerIdentityDashProfiles.aeba67850e106299f25de2eb3828c641".replace(
    " ", ""
)


def get_username(navigation_url):
    """returns username from navigation url

    Args:
        navigation_url (str): "https://www.linkedin.com/in/benjamin-cowen-28579430?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAAaFyYUBZBFlPRrb0LRvazdX-ggWT6pu-Pk"

    Returns:
        str: username
    """
    profile_url = navigation_url.split("?")[0]
    username = profile_url.split("/")[-1]
    return username


def get_profile_from_db(username):
    profiles = find_documents(
        constants.MongodbCollections.PROFILES, {"username": username}
    )
    if profiles:
        return profiles[0]
    return True


def get_fsd_profile_id(username):
    profile = get_profile_from_db(username)
    if profile:
        # entity_urn -> urn:li:fsd_entityResultViewModel:(urn:li:fsd_profile:ACoAABwnuU8BzinoZuAFK8xDgSadSAO5BAzKAeE,SEARCH_SRP,DEFAULT)
        entity_urn = profile["entityUrn"]
        fsd_profile_match = re.search(constants.FSD_PROFILE_REGEX, entity_urn)
        fds_profile_id = fsd_profile_match.group(1)
        return fds_profile_id
    return None


def get_profile_contact(username):
    return send_request(
        "get",
        f"https://www.linkedin.com/voyager/api/graphql?includeWebMetadata=true&variables=(memberIdentity:{username})&queryId=voyagerIdentityDashProfiles.c7452e58fa37646d09dae4920fc5b4b9",
    )


def get_profile(url=None, username=None):
    if url:
        username = get_username(url)

    filled_variables = variables.format(username)

    status_code, data = send_request(
        "get",
        f"https://www.linkedin.com/voyager/api/graphql?variables={filled_variables}",
    )
    if status_code == constants.status.HTTP_200_OK:
        upsert_document(
            constants.MongodbCollections.PROFILES,
            {"username": username},
            data={"details": data["included"]},
            specific_field_update=True,
        )
    return status_code, data


if __name__ == "__main__":
    # status_code, data = get_profile_contact("aditya-prasad-9a785a46")
    # print("➡ src/profile_details.py:53 status_code:", status_code)
    # print("➡ src/profile_details.py:54 data:", data)

    status_code, data = get_profile("gdbowling")
    print("➡ src/profile_details.py:53 status_code:", status_code)
    print("➡ src/profile_details.py:54 data:", data)
