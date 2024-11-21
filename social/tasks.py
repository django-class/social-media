from .services import SocialServiceFactory


factory = SocialServiceFactory()



youtube_service = factory.create_service("youtube")
youtube_service.get_list_of_videos_from_channel()