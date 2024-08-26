from helper import constants
from helper.request_handler import send_request

variables = "(\
    profileUrn:urn%3Ali%3Afsd_profile%3A{0},\
    sectionType:{1},\
    locale:en_US)\
    &queryId=voyagerIdentityDashProfileComponents.7af5d6f176f11583b382e37e5639e69e".replace(
    " ", ""
)


def list_section(fsd_profile, section_type):
    filled_variables = variables.format(fsd_profile, section_type)
    status_code, data = send_request(
        "get",
        f"https://www.linkedin.com/voyager/api/graphql?variables={filled_variables}",
    )
    return status_code, data


if __name__ == "__main__":

    status_code, data = list_section(
        fsd_profile="ACoAAADX4y8Bmz9cGMop-8CZzNkXNgBO29WU708",
        section_type=constants.LinkedinSectionTypes.EXPERIENCE,
    )
    print("➡ src/list_user_section.py:36 status_code:", status_code)
    print("➡ src/list_user_section.py:37 data:", data)
