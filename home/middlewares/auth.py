from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.
    print("initialize...")
    def middleware(request):
        return_url = request.META.get('PATH_INFO')
        print("-------->>", return_url)
        if not request.session.get('uid'):
            return redirect('login')
        response = get_response(request)
        return response

    return middleware