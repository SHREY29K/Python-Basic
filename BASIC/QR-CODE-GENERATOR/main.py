import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
svg_img = qrcode.make("Hi! I'm Shrey Kothari", image_factory=factory)
svg_img.save("myQR.svg")