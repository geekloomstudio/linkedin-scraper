import logging
import time
import traceback

import requests

from config import cookies, headers
from helper.constants import methods, status


def send_request(
    method,
    url,
    headers=headers,
    cookies=cookies,
    json_data=None,
    params=None,
    data=None,
    timeout=10,
    retry=0,
    retry_duration=3,
):
    error = None
    while True:
        try:
            request_method = getattr(requests, method)
            payload = {
                "url": url,
                "headers": headers,
                "cookies": cookies,
                "json": json_data,
                "data": data,
                "timeout": timeout,
                "params": params,
            }
            if method in [methods.HTTP_GET, methods.HTTP_DELETE]:
                payload.pop("json")
                payload.pop("data")

            if not params:
                payload.pop("params")

            response = request_method(**payload)
            logging.info("response.status_code: %s", response.status_code)

            if response.status_code in [
                status.HTTP_500_INTERNAL_SERVER_ERROR,
                status.HTTP_501_NOT_IMPLEMENTED,
                status.HTTP_502_BAD_GATEWAY,
                status.HTTP_503_SERVICE_UNAVAILABLE,
                status.HTTP_504_GATEWAY_TIMEOUT,
                status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED,
            ]:
                return response.status_code, response.content
            else:
                return response.status_code, response.json()
        except Exception:
            error = traceback.format_exc()
            logging.exception(error)
            retry -= 1
            time.sleep(retry_duration)

        if retry <= 0:
            break
    return None, error
