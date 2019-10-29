# overlay
2 files overlay

## Background image
![Background](https://github.com/pydemo/overlay/blob/master/in/Gergiev_art_helps_putin_to_kill.jpg?raw=true)

## Foreground image
![Foreground](https://github.com/pydemo/overlay/blob/master/in/gergiev_is_war_supporter.JPG?raw=true)


## Get images width/height
```
b_h, b_w, b_ch = background.shape

o_h, o_w, o_ch = overlay.shape

```

## Scale background image
```
    W = 800
    imgScale = W/b_w
    new_b_h,new_b_w = int(b_h*imgScale), int(b_w*imgScale)
    new_background = cv2.resize(background,(new_b_w, new_b_h))
```

## Overlay 2 images
```
    #OVERLAY
    OPACITY = 0.7
    added_image = cv2.addWeighted(new_background,0.6,square,0.4,0)
    cv2.imshow('adjusted', added_image)  
    cv2.waitKey()
    cv2.imwrite(out, added_image)
```

## Overlay image
![test](https://github.com/pydemo/overlay/blob/master/out/Gergiev_art_helps_putin_to_kill_gergiev_is_war_supporter.JPG?raw=true)
