from django.template import Library

from world_traveller.profiles.models import Profile

register = Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    """
    TemplateTag is created to show that a user's
    profile is not totally completed.
    """
    is_complete = True
    if context.request.user.id:
        profile = Profile.objects.get(pk=context.request.user.id)

        is_complete = profile.is_complete

    return {
        'is_complete': is_complete,
    }