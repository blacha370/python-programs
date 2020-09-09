from PIL import Image

class ImageEditor:
    @staticmethod
    def iterateImages(photos_list: list, logo_path: str, directory_path: str, position: list):
        logo = Image.open(logo_path)
        for photo in photos_list:
            if photo.endswith('.png') or photo.endswith('.jpg') or photo.endswith('.jpeg') or photo.endswith('.jpe') or photo.endswith('.jfif') or photo.endswith('.exif'):
                img = Image.open(directory_path + '/' + photo)
                size = img.size
                if size[0] < position[0] + logo.size[0]:
                    position[0] = size[0] - logo.size[0]
                if size[1] < position[1] + logo.size[1]:
                    position[1] = size[1] - logo.size[1]
                img.paste(logo, tuple(position), logo)
                img.save(directory_path + '/withlogo/' + photo)
