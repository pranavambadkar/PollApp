from pollapp.models import SocialMedia

def social_media_links(request):
    links = SocialMedia.objects.all()
    return {'social_links': links}