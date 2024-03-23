from PIL import Image
#ASCII characters which will makeup the image
ASCII_C=["@","#","$","%","?","!","*","+",";",":",",","."]

# Resize function to change the dimensions of the image
def resize(image,new_width=100):
    width,height=image.size
    ratio=height/width
    new_height=int(ratio*new_width)
    resize_image=image.resize(((new_width+200),new_height))
    return resize_image

# greyscale to change each pixel in the image to the its luminance
def greyscale(image):
    new_image=image.convert("L")
    return new_image

# this function will assign value to each pixel ranging from 0 to mumber fo character in the ASCII string
def pixel_to_ASCII(image):
    pixels=image.getdata()
    charac="".join([ASCII_C[pixel//22] for pixel in pixels])
    return charac 

 # this is where we we will do the printing and inputing the file path   
def main(new_width=300):
    path=input("Enter the path of the image:\n")
    try:
        image=Image.open(path)
    except:
        print("Enter a valid path.\n")
    
     
    
    ascii_str = pixel_to_ASCII(greyscale(resize(image)))
        
    pixel_co=len(ascii_str)
    ascii_img="\n".join(ascii_str[i:(i+new_width)] for i in range(0,pixel_co,new_width))
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)

    print("ASCII art written to ascii_image.txt")
       

   
main()
        