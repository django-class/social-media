from abc import ABC, abstractmethod



class SocialServiceInterface(ABC):

    @abstractmethod
    def get_list_of_videos_from_channel():
        pass



class YoutubeService(SocialServiceInterface):
    
    def get_list_of_videos_from_channel(self):
        print(" Lista de Videos do Youtube ")

    def list_videos_from_xml(self, xml):
        pass


class InstagramService(SocialServiceInterface):
    
    def get_list_of_videos_from_channel(self):
        print(" Lista de Videos do Instagram ")

    def list_videos_from_xml(self, xml):
        pass



class SocialServiceFactory:

    @staticmethod
    def create_service(platform: str) -> SocialServiceInterface:
        if platform=="youtube":
            service = YoutubeService()
        elif platform=="instagram":
            service = InstagramService()
        else:
            raise ValueError(f"Plataforma desconhecida {platform}")
        




