def makeHTML(contents):
    slides = len(contents)
    slides_html = """<li data-app-prevent-settings="" data-target="#slider1-5" class=" active" data-slide-to="0"></li>"""
    for slide in range(1, slides):
        slides_html += f"""<li data-app-prevent-settings="" data-target="#slider1-5" data-slide-to="{slide}"></li>"""
    content_html = """"""
    state = " active"
    for content in contents:
        content_html += f"""
        <div class="carousel-item slider-fullscreen-image{state}" data-bg-video-slide="false" style="background-image: url(assets/images/download-1280x720.jpg);">
                    <div class="container container-slide">
                      <div class="image_wrapper">
                        <div class="mbr-overlay"></div>
                        <img src="assets/images/download-1280x720.jpg">
                        <div class="carousel-caption justify-content-center">
                          <div class="col-10 align-left"><p class="lead mbr-text mbr-fonts-style display-7">{content}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>"""
        state = ""
    html = f"""<!DOCTYPE html>
    <html  >
    <head>
      <!-- Site made with Mobirise Website Builder v4.9.7, https://mobirise.com -->
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="generator" content="Mobirise v4.9.7, mobirise.com">
      <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
      <link rel="shortcut icon" href="assets/images/logo4.png" type="image/x-icon">
      <meta name="description" content="">

      <title>Home</title>
      <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css">
      <link rel="stylesheet" href="assets/tether/tether.min.css">
      <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css">
      <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css">
      <link rel="stylesheet" href="assets/theme/css/style.css">
      <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">



    </head>
    <body>
      <section class="carousel slide cid-rovAEPohEC" data-interval="false" id="slider1-5">



        <div class="full-screen">
          <div class="mbr-slider slide carousel" data-pause="true" data-keyboard="false" data-ride="false" data-interval="false">
            <ol class="carousel-indicators">
              {slides_html}
            </ol>
            <div class="carousel-inner" role="listbox">
              {content_html}
            </div>
            <a data-app-prevent-settings="" class="carousel-control carousel-control-prev" role="button" data-slide="prev" href="#slider1-5">
              <span aria-hidden="true" class="mbri-left mbr-iconfont"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a data-app-prevent-settings="" class="carousel-control carousel-control-next" role="button" data-slide="next" href="#slider1-5">
              <span aria-hidden="true" class="mbri-right mbr-iconfont"></span>
              <span class="sr-only">Next</span>
            </a>
          </div></div>

    </section>


      <section class="engine"><a href="https://mobirise.info/p">site templates free download</a></section><script src="assets/web/assets/jquery/jquery.min.js"></script>
      <script src="assets/popper/popper.min.js"></script>
      <script src="assets/tether/tether.min.js"></script>
      <script src="assets/bootstrap/js/bootstrap.min.js"></script>
      <script src="assets/ytplayer/jquery.mb.ytplayer.min.js"></script>
      <script src="assets/vimeoplayer/jquery.mb.vimeo_player.js"></script>
      <script src="assets/bootstrapcarouselswipe/bootstrap-carousel-swipe.js"></script>
      <script src="assets/smoothscroll/smooth-scroll.js"></script>
      <script src="assets/theme/js/script.js"></script>
      <script src="assets/slidervideo/script.js"></script>


    </body>
    </html>"""
    return html
