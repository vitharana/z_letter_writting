from Z_Scanner import Z_Scanner
import cv2


z_scanner = Z_Scanner()

pixel_locations = z_scanner.read_image_grayscale_vertically('output_image0.jpg')



#z_scanner.find_line_thickness()
#z_scanner.draw_top_line()
pixels_of_z = z_scanner.get_total_z_coordinates()
blank_img = z_scanner.create_blank_img()
z_scanner.draw_shape(pixels_of_z)


while True:


    no_div , locations = z_scanner.add_defect_on_location(pixels_of_z,allowed_d_loc= 5,allowed_d_pixs= 25)
    no_div = int(no_div)
    print(no_div,locations)



    new_defected_set = pixels_of_z


    for i in range(len(locations)):
        new_defected_set = z_scanner.add_defects(new_defected_set,div=no_div,defect_pos=locations[i])




    #z_scanner.draw_shape(new_defected_set,'DefZ',time_out=0)
    image = z_scanner.draw_shape_save(new_defected_set, 'DefZ', time_out=10)
    cv2.waitKey(1000)
    #z_scanner.save_img(image)

