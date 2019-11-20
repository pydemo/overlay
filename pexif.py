from exif import Image
fn=r'in\Hibla_gerzmava_is_a_war_supporter.JPG'
with open(fn, 'rb') as image_file:
	my_image = Image(image_file)

print(my_image.has_exif)