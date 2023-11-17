from django.core.exceptions import PermissionDenied


def check_user_positions(user, allowed_positions):
    if not user.profile.is_position_allowed(allowed_positions):
        raise PermissionDenied("You don't have permission for this action.")
