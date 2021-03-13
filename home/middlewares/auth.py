from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.
    print("initialize...")
    def middleware(request, id):
        return_url = request.META['PATH_INFO']
        if not request.session.get('uid'):
            return redirect(f'login?return_url={return_url}')
        response = get_response(request)
        return response

    return middleware