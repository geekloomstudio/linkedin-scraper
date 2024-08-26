from helper import constants
from helper.decorators import sleep
from helper.request_handler import send_request
from profile_details import get_fsd_profile_id, get_profile
from services.mongodb.pymongo_client import find_documents

params = {
    "action": "verifyQuotaAndCreateV2",
    "decorationId": "com.linkedin.voyager.dash.deco.relationships.InvitationCreationResultWithInvitee-2",
}

json_data = {
    "invitee": {
        "inviteeUnion": {
            "memberProfile": "urn:li:fsd_profile:{0}",
        },
    },
}


@sleep(1, 3)
def send_connection(fsd_profile_id):
    json_data["invitee"]["inviteeUnion"]["memberProfile"] = json_data["invitee"][
        "inviteeUnion"
    ]["memberProfile"].format(fsd_profile_id)

    return send_request(
        "post",
        "https://www.linkedin.com/voyager/api/voyagerRelationshipsDashMemberRelationships",
        params=params,
        json_data=json_data,
    )


def connect_all_users():
    non_connected_users = find_documents(
        constants.MongodbCollections.PROFILES,
        {
            "details": {
                "$elemMatch": {
                    "memberRelationshipDataResolutionResult.noInvitation": {
                        "$exists": True,
                        "$ne": None,
                    }
                }
            }
        },
        projection={"username": True},
    )
    print("➡ src/connect_user.py:49 non_connected_users:", len(non_connected_users))
    for user in non_connected_users:
        fsd_profile_id = get_fsd_profile_id(user["username"])
        if fsd_profile_id:
            print("➡ src/connect_user.py:57 fsd_profile_id:", fsd_profile_id)
            print(user["username"])
            status_code, data = send_connection(fsd_profile_id)
            print("➡ src/connect_user.py:53 status_code:", status_code)
            print("➡ src/connect_user.py:54 data:", data)
            if status_code in [
                constants.status.HTTP_200_OK,
                constants.status.HTTP_400_BAD_REQUEST,
            ]:
                get_profile(user["username"])


if __name__ == "__main__":
    connect_all_users()
