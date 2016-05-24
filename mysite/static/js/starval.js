$(function(){
    var star_length = 5;  // 星の数
    var star_size = 32;   // 星のサイズ(px)
    $(".star-value").each(function(){
        var i, fixed, container = $(this);
        
        // 枠
        star_val.css({
            width: star_size * star_length,
            height: star_size,
            backgroundPositionX: -star_size * star_length
        });
        
        // 判定用ブロック
        for(i = 0; i < star_length; i++){
            $("<div></div>")
                .css({
                    width: star_size,
                    height: star_size,
                })
                .appendTo(container);
        }
        
        // イベント
        container.find("div")
            .on("mouseenter", function(){
                if(fixed) return;
                container.css("background-position-x", 
                    star_size * ($(this).index() + 1 - star_length));
            })
            .on("mouseleave", function(){
                if(fixed) return;
                container.css("background-position-x", -star_size * star_length);
            })
            .on("click", function(){
                fixed = true;
                container.css("background-position-x", 
                    star_size * ($(this).index() + 1 - star_length));
                $(".debug").html(container.attr("name") + " Valued: " + ($(this).index() + 1));
            });
    });
});