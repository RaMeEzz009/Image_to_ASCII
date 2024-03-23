from PIL import Image

ASCII_C=["@","#","$","%","?","!","*","+",";",":",",","."]


def resize(image,new_width=100):
    width,height=image.size
    ratio=height/width
    new_height=int(ratio*new_width)
    resize_image=image.resize(((new_width+200),new_height))
    return resize_image


def greyscale(image):
    new_image=image.convert("L")
    return new_image


def pixel_to_ASCII(image):
    pixels=image.getdata()
    charac="".join([ASCII_C[pixel//22] for pixel in pixels])
    return charac 

    
def main(new_width=300):
    path=input("Enter the path of the image:\n")
    try:
        image=Image.open(path)
    except:
        print("Enter a valid path.\n")
    
    
    image = resize(image)
    image = greyscale(image)
    ascii_str = pixel_to_ASCII(image)
        
    pixel_co=len(ascii_str)
    ascii_img="\n".join(ascii_str[i:(i+new_width)] for i in range(0,pixel_co,new_width))
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    print("ASCII art written to ascii_image.txt")
       

   
main()
        