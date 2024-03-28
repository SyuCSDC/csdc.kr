from .models import Mentorship

def mentorship_participation(request):
    user_profile = request.user.userprofile if request.user.is_authenticated else None
    is_participant = False
    if user_profile:
        is_participant = Mentorship.objects.filter(
            mentor=user_profile).exists() or Mentorship.objects.filter(
            mentee=user_profile).exists()
    return {'is_participant': is_participant}
