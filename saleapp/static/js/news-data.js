const hotTours = [
    {
        name: 'Sapa - Mộc Châu',
        star: 5,
        review: 325,
        date: '10/10/2021',
        priceText: '7.500.000đ',
        period: '4 ngày 3 đêm',
        number: 9
    },
    {
        name: 'Đà Nẵng',
        star: 5,
        review: 362,
        date: '11/10/2021',
        priceText: '3.500.000đ',
        period: '3 ngày 2 đêm',
        number: 2
    },
    {
        name: 'Hội An',
        star: 5,
        review: 300,
        date: '9/10/2021',
        priceText: '5.499.000đ',
        period: '5 ngày 4 đêm',
        number: 3
    },
    {
        name: 'Đà Lạt',
        star: 5,
        review: 410,
        date: '21/10/2021',
        priceText: '1.999.000đ',
        period: '3 ngày 2 đêm',
        number: 2
    },
    {
        name: 'Nha Trang',
        star: 5,
        review: 379,
        date: '31/10/2021',
        priceText: '2.999.000đ',
        period: '2 ngày 1 đêm',
        number: 4
    },
    {
        name: 'Phú Quốc',
        star: 5,
        review: 450,
        date: '12/10/2021',
        priceText: '4.499.000đ',
        period: '3 ngày 2 đêm',
        number: 5
    }
]

const handBooks = [
    {
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457926/monan_zu9svb.jpg',
        name: 'Du lịch Cần Giờ ăn gì, quán nào ngon?',
        date: '26/09/2021',
        info: `<p><b>Bên cạnh những món hải sản tươi ngon như tôm tít, ghẹ, hàu... du lịch Cần Giờ bạn nhất
                        định đừng bỏ qua những món 'đặc sản' này nhé:</b></p>
                <p><b>+ Cá thòi lòi trộn gỏi lìm kìm:</b> Món ăn dân dã với vị béo thơm của cá thòi lòi, vị
                    chua chua chát chát của lá lìm kìm lẫn trong vị ngọt của nước mắm pha đường thiệt là
                    ngon hết sẩy. Và sẽ càng ngon hơn khi các bạn thưởng thức với rượu mật ong rừng Sác.</p>
                <p><b>+ Cơm cháy chà bông:</b> Tại Cần Giờ có cách chế biến món cơm cháy chà bông khá lạ, vì
                    thế món ăn này còn được nhiều người bảo nhau là 'đặc sản' của du lịch Cần Giờ. Xôi được
                    cán mỏng, bọc quanh hỗn hợp nhân là thịt ốc và gia vị, tạo thành hình bánh gối. Món bánh
                    này được chiên giòn, ăn cùng chà bông rất thơm ngon khiến người ăn ăn một lần là thèm
                    thuồng mãi.</p>
                <p><b>+ Các món hải sản:</b> tôm là loại hải sản được yêu thích nhất với nhiều cách chế biến
                    khác nhau từ nướng, hấp, cho đến luộc. Bên cạnh đó, những món như gỏi xoài ốc giác, ốc
                    móng chân, nghêu xào lá buôi, ốc mỡ hấp sả... cũng là món hảo của rất nhiều du khách.
                </p>
                <p><b>Du lịch Cần Giờ bạn nên tìm đến những quán ăn gợi ý sau đây để thưởng thức được những
                        món hải sản ngon nhất với giá cả hợp lý:</b></p>
                <p><b>+ Chợ hải sản Hàng Dương:</b> Nói đến ăn gì ở Cần Giờ thì người ta sẽ trả lời ngày là
                    vào chợ Hàng Dương ăn hải sản. Nằm cách biển 30/4 chỉ khoảng 50m, nơi đây có buôn bán
                    nhiều loại hải sản tươi ngon và đa dạng như ốc, tôm, cá, cua mực, ghẹ…. Trong khu vực
                    chợ Hàng Dương có cực nhiều các quán hải sản ngon ở Cần Giờ. Bạn có thể ăn ngay tại quán
                    hoặc là mang ra biển ngồi hóng gió biển.</p>
                <p><b>+ Quán Thanh Lịch:</b> Đây là một trong những quán hiếm ai khi đến Cần Giờ có thể bỏ
                    qua được bởi vì hải sản ở quán này rất tuyệt vời, tất cả các món đều có hương vị riêng
                    được nhiều người khen ngợi. Bạn có thể trực tiếp lựa chọn những loại hải sản mà mình
                    muốn ăn, hay những loại hải sản mà bạn cảm thấy tươi ngon nhất để nhờ đầu bếp của quán
                    chế biến.</p>
                <p><b>+ Quán hải sản Chú 5 Lùn:</b> Nổi tiếng với tươi ngon, ngọt thịt mang đậm hương vị của
                    biển cả. Ghé thăm quán bạn sẽ được thưởng thức đủ các món hải sản như ghẹ, tôm, cua, ốc
                    và đặc biệt là con cúm (con cua) rất ngon.</p>`
    },
    {
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457926/nhahang_twtqac.jpg',
        name: 'Top 5 nhà hàng Việt Nam ngon ở Sài Gòn níu chân du khách.',
        date: '24/09/2021',
        info: `<p><b>Thật khôn ngoa khi nói Sài Gòn là một thiên đường ẩm thực. Sài Gòn là nơi giao thoa
                    của nhiều nền văn hóa độc đáo và đặc sắc, vì thế nền ẩm thực nơi đây cũng vô cùng đa
                    dạng. Giữa vô vàn nhà hàng phục vụ ẩm thực các nước trên thế giới, nhưng nhà hàng
                    món ăn Việt Nam vẫn luôn là điểm đến yêu thích của nhiều thực khách.</b></p>
                <p><b>+ Nhà hàng Hội An Sense:</b> Là một trong những nhà hàng Việt Nam ngon ở Sài Gòn mang
                    đến thực khách hương vị đúng chuẩn đặc sản miền Trung. Thực đơn của nhà hàng là các món
                    ăn nổi tiếng gắn liền với vùng đất Hội An như cao lầu, chả giò Hội An, cơm hến, cơm hấp
                    lá sen, bánh hoa hồ…</p>
                <p><b>+ Nhà hàng Cục Gạch Quán:</b> Nếu muốn tìm lại hương vị quê nhà giữa phố phường tấp
                    nập của Sài Gòn, hãy đến ngay nhà hàng Cục Gạch Quán. Thực đơn của quán có đủ món thuần
                    Việt nấu theo đặc trưng ẩm thực ba miền Bắc – Trung – Nam cho bạn lựa chọn. Cách trình
                    bày món ăn ở đây cũng mộc mạc với chén đất nung, gói lá chuối, nồi đất… vốn là những vật
                    dụng quen thuộc với người Việt Nam.</p>
                <p><b>+ Quán Bụi – Original:</b> Là một trong năm nhà hàng thuộc hệ thống Quán Bụi, Quán Bụi
                    Original thu hút thực khách không chỉ trong nước mà cả khách nước ngoài bởi thực đơn với
                    các món đặc sản Việt Nam hấp dẫn. Ở Quán Bụi Original hội tụ các món ăn truyền thống từ
                    Nam ra Bắc, như thịt kho cơm dừa, phở cuốn, bông bí xào tỏi, canh riêu thì là… Ngoài ra,
                    Quán Bụi Original còn hấp dẫn thực khách bởi không gian yên tĩnh, lịch sự, ấm cúng và
                    sang trọng. Nhà hàng được trang trí theo phong cách Sài Gòn xưa, nên khi đến đây bạn sẽ
                    như được trở về một Sài Gòn của những năm 1980. Phong cách này của nhà hàng cũng là điểm
                    nhấn thu hút khách nước ngoài, hoặc nếu bạn tiếp đối tác nước ngoài thì Quán Bụi
                    Original cũng là sự lựa chọn lý tưởng.</p>
                <p><b>+ Khoái:</b> Nếu bạn là tín đồ của ẩm thực Nha Trang thì Khoái chính là điểm đến dành
                    riêng cho bạn rồi đấy. Nhà hàng Khoái chuyên phục vụ các món đặc sản nổi tiếng của thành
                    phố biển Nha Trang như bánh căn, bún sứa, bánh bèo tôm chấy, nem nướng Ninh Hòa, gỏi cá
                    mai, gỏi sứa… Ngoài ra, đến đây bạn còn có thể thưởng thức những món hải sản tươi sống
                    được chế biến hấp dẫn như nấu lẩu, trộn gỏi, nướng, hấp…</p>
                <p><b>+ Bếp Nhà Lục Tỉnh:</b> là một nhà hàng Việt Nam ngon ở Sài Gòn mà bạn nên đến nếu
                    muốn thưởng thức ẩm thực miền Tây. iên điển xào tép đồng, ốc bươu nướng tiêu xanh, bánh
                    xèo thịt vịt củ hũ dừa… đều là những món được chế biến với nguyên liệu tươi ngon, hương
                    vị đậm chất miền Tây. Bước vào Bếp Nhà Lục Tỉnh, bạn như được đến một miền Tây thu nhỏ
                    với không gian được thiết kế và trang trí một cách chân quê, mộc mạc và tao nhã, sang
                    trọng. Mọi ngóc ngách trong nhà hàng đều được chăm chút tỉ mỉ. Không gian rộng lớn, có
                    giếng trời và khoảnh sân trang trí hồ nước, với thuyền với hoa… khiến thực khách khi đến
                    đây dường như trút bỏ được mọi ưu phiền, mệt mỏi thường nhật.</p>`
    },
    {
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457925/monNgon_b1bu6r.jpg',
        name: 'Loạt món ngon Hà Nội những ngày cuối thu được lòng thực khách.',
        date: '20/09/2021',
        info: `<p><b>Với nhiều khách du lịch Hà Nội, họ yêu mùa se lạnh nơi đây không chỉ bởi cái lãng mạn
                    của của phố xá vào thu lá vàng rơi rụng, phố cổ dường như cổ hơn mà còn vì loạt món
                    ngon này:</b></p>
                <p><b>+ Ốc luộc:</b> Du lịch Hà Nội vào những ngày cuối thu trời se lạnh, dạo quanh Hồ Tây,
                    góc phố để tìm gì đó ngon ngon “cho vào bụng” thì ốc luôn là lựa chọn hàng đầu. Ốc luộc
                    Hà Nội có vị ngọt, bùi, dai giòn, chấm cùng nước mắm chanh, sả, ớt chua ngọt, dậy mùi
                    gừng thơm nồng. Những ngày này nếu được ngồi cùng bạn bè, những người mình thương yêu,
                    vừa trò chuyện rôm rả vừa thưởng thức món ốc nóng hổi thì sẽ chẳng còn gì ngon hơn!</p>
                <p><b>+ Thịt xiên nướng:</b> được xem là món ăn đường phố hấp dẫn bậc nhất ở Hà Nội. Ngày
                    trời lạnh dần, những quán cóc ven đường nghi ngút khói, thơm ngậy mùi thịt nướng, đủ sức
                    hấp dẫn làm níu chân những thực khách qua đường. Những miếng thịt vàng ươm, chảy mỡ béo
                    ngậy được tẩm ướp tinh tế đủ vị: ngọt, mặn, cay… Khi ăn, thực khách có thể ăn kèm thịt
                    xiên với bánh mì giòn rụm hoặc chấm với tương ớt đều rất thơm ngon.</p>
                <p><b>+ Bún riêu:</b> Nhớ đến Hà Nội là nhớ đến bún riêu, thứ quà sáng giản đơn mà tinh tế,
                    quyến luyến trong một buổi sáng mát trời. Mặc dù nguyên lieeij làm bún riêu của người Hà
                    Nội có sự thay đổi qua nhiều năm nhưng phần nước dùng vẫn là vị chua dịu của giấm bỗng
                    cùng cà chua làm nổi lên vị ngọt nhẹ của cua đồng. Nhìn nồi nước dùng đỏ au màu cà chua,
                    lấp lánh những tảng riêu cua vàng rực bốc khói, thật sự khó kiềm lòng được.</p>
                <p><b>+ Nem chua rán:</b> Buổi tối dạo chơi Hà Nội, cầm trên tay que nem chua rán thưởng
                    thức thì phải nói là ngon đúng chuẩn luôn. Nem chua rán giòn ngoài vỏ mà bên trong vẫn
                    mềm, chấm thêm tí tương ớt hoặc tương cà, thưởng thức kèm với rau sống để thêm tròn vị
                    làm bao khách du lịch Hà Nội mê mẩn ngay từ lần đầu thưởng thức.</p>
                <p><b>+ Bánh đúc nóng:</b> Có thể có nhiều thực khách đã từng thưởng thức qua món bánh đúc
                    nóng ở rất nhiều nơi, nhưng một khi đã đi du lịch Hà Nội thì vẫn cứ hoài tìm và thưởng
                    thức món bánh đúc nóng ở đây cho bằng được. Một bát đầy đặn bao gồm phần bánh dẻo quánh,
                    thịt băm xào mộc nhĩ giòn tươi, dậy mùi bởi hành phi thơm phức. Tất cả hòa quyện cùng
                    nước dùng đậm đà mang đến cho bạn một hương vị thật khác biệt chỉ muốn thưởng thức một
                    bát nữa mới thôi.</p>
                <p><b>+ Bánh chưng rán:</b> Vào những ngày trời trở gió cuối thu đầu đông, thật không khó để
                    tìm gặp những quán bán bánh chưng rán nhỏ xinh như thế này ở phố phường Hà Nội. Dù vừa
                    béo vừa ngấy, nhưng hơi ấm từ trong lòng bánh, hương thơm của lá chuối, của thịt, đỗ
                    xanh hòa quyện cùng nếp, vẫn đủ sức 'nịnh' chiếc bụng đói của nhiều người. Bánh chưng
                    rán thường được ăn kèm với dưa góp, đu đủ, cà rốt, rưới thêm chút tương ớt hay xì dầu.
                </p>`
    }
]

const experiences = [
    {
        name: 'Một vài kinh nghiệm đi du lịch biển mà bạn cần biết.',
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457927/phuquoc_cys1zd.jpg',
        info: `<p><b>Khung cảnh thiên nhiên hoang sơ, hùng vĩ, huyền bí nhưng cũng không kém phần thơ mộng.
                Trải dài từ Bắc – Nam là sự vỗ về ấm áp, những con sóng nhấp nhô, dập dờn theo triền đá,
                bờ cát êm dịu cùng ánh nắng ngập tràn bình yên … Chỉ ngần ấy thôi cũng đủ làm lòng ta
                xao xuyến mỗi khi nghĩ tới biển và muốn xách ba lô lên và đi ngay phải không nào?</b>
                </p>
                <p><b><i> 1, Lựa ý khi tắm biển:</i></b> Trước khi xuống biển, bạn nên dành khoảng 5 -10 phút để
                    quan sát mặt biển nhé. Nhớ khởi động cơ thể trước khi tắm nhưng cũng không nên tập quá sức
                    bạn nhé! Và khi xuống nước bạn không nên ào ào lao mình xuống ngay. Và nên lưu ý là lần
                    xuống nước đầu tiên tuyệt nhiên không quá 15 phút. Vui thôi đừng vui quá! Không đi xa bờ quá
                    15m hoặc đến những nơi có mực nước sâu quá 5m. Không nên ăn quá no hoặc để bụng quá đói
                    trước khi xuống biển. Khi có các triệu chứng nhứ: ngứa ngáy, đột nhiên trở lạnh hay mệt mỏi
                    bất thường, nhức đầu hoặc sau gáy, bị chuột rút, chướng bụng, đau khuỷu tay, đầu gối,… thì
                    cần lên bờ ngay.</p>
                <p><b><i>2, Những dụng cụ cần mang theo khi du lịch biển:</i></b></p>
                <p><b>+ Người lớn: </b>Vì thời tiết ở biển mùa hè thường rất nắng nóng nên kem chống nắng, đồ
                    bơi là những thứ không thể thiếu nhé! Khăn lông, khăn choàng, kính râm (không chỉ giúp bạn
                    bảo vệ đôi mắt mà còn có thể tận dụng để có thể có những shoot ảnh đẹp). Kính bơi, đồ lót.
                    Mỹ phẩm (dầu gội, sữa tắm, sữa rửa mặt, xịt khoáng,..) Thuốc (có thể giúp bạn sơ cứu kịp
                    thời từ việc di chuyển bằng xe, đi thuyền hay lướt sóng …). Phụ kiện chụp ảnh (gậy selfie và
                    túi chống nước điện thoại, sạc dự phòng…).</p>
                <p><b>+ Trẻ em: </b>Đồ tắm, khăn lông, khăn giấy ướt, tã giấy, bỉm (&lt;2 tuổi).Xe đẩy, quần áo
                    ngoài, đồ lót, tất, yếm (ngày &amp; đêm), áo quần ấm. Phao, kính và mũ bơi, kem chống nắng,
                    chống côn trùng. Sữa bột, bình và dụng cụ pha sữaDầu tắm, gội và đồ dùng vệ sinh của bé…</p>
                <p><b><i>3, Một số mẹo nhỏ khi du lịch biển:</i></b></p>
                <p><b>+Khi bị sứa cắn: </b>Nhanh chóng lên bờ, rời khỏi vùng biển đang bơi. Rửa vùng da bị sứa
                    cắn với giấm. Có thể gỡ bằng nhíp hoặc bằng tay (phải đeo găng) nếu thấy xúc tu của sứa vẫn
                    còn dính trên da. Trong vòng 20-40 phút, nên ngâm vùng da bị cắn vào nước ấm (40-45 độ C).
                    Nếu có cảm giác ngứa và sưng phù nhiều, có thể bôi kem chứa corticoid hoặc uống thuốc kháng
                    histamin. Tiếp tục theo dõi vết cắn những ngày sau đó, nếu không thuyên giảm thì nên nhanh
                    chóng đến bác sĩ.</p>
                <p><b>+Cách chống say xe hiệu quả:</b> Trước ngày đi, bạn nên ngủ đủ giấc và đừng ăn quá no. Một
                    số loại thực phẩm giúp chống say xe: Ngũ cốc, bánh mì sandwich, trái cây khô, sữa đậu nành,
                    bánh quy giòn, nước. Nên tránh uống thức uống có ga. Uống thuốc chống say hoặc có thể dùng
                    dấm, gừng tươi và vỏ quýt vì cũng có thể giúp chống say xe hiệu quả. Nên ngồi ghế trước và
                    hạn chế đọc sách báo, sử dụng điện thoại, nên trò chuyện với mọi người xung quanh. Nên trang
                    bị túi dự phòng để phòng trường hợp bất trắc bạn nhé!</p>`
    },
    {
        name: 'Những kinh nghiệm đi du lịch miền núi phía Bắc.',
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457924/blog_3_pzquxr.jpg',
        info: `<p><b> Trong rất nhiều địa điểm du lịch Việt Nam, các tỉnh miền núi phía Bắc là điểm đến vô cùng
                    hấp dẫn bao gồm những nét phong tục, văn hóa mới lạ gây nhiều hứng thú và bởi cảnh sắc
                    thiên nhiên hùng vĩ làm say mê lòng người. Afforda xin chia sẻ một số kinh nghiệm du
                    lịch miền núi phía Bắc trong bài viết sau đây:</b></p>
                <p><b><i> 1, Lựa chọn địa điểm:</i></b> Các tỉnh miền núi phía Bắc có rất nhiều địa danh nổi
                    tiếng thu hút lượng lớn khách du lịch như: Sapa, Y Tí, Bắc Hà (Lào Cai), Tà Xùa, Mộc Châu
                    (Sơn La), Hà Giang, Mù Cang Chải (Yên Bái), Điện Biên, Lai Châu…. Những lịch trình một điểm
                    đến như này phù hợp cả với du lịch tour và du lịch phượt. Với các địa điểm du lịch ở các
                    tình miền núi này thì việc lựa chọn không hề khó, tưởng như lựa chọn bất cứ nơi đâu bạn cũng
                    không hề sai, nơi đâu cũng đẹp, cũng lạ, chỉ quan trọng là bạn thích đâu hơn hay đâu tiện
                    hơn mà thôi.</p>
                <p><b><i>2, Lựa chọn thời gian đi du lịch:</i></b> Thường mùa du lịch ở đây rơi vào khoảng cuối
                    tháng 8, đầu tháng 9 đến tháng 12 dương lịch và sau dịp Tết Nguyên Đán âm lịch. Đây là
                    khoảng thời gian mà trời Tây Bắc, Đông Bắc đẹp nhất, dễ chịu nhất, ít mưa, nắng không quá
                    nhiều. Đây cũng là lúc diễn ra nhiều lễ hội và là mùa của các loại hoa nở như hoa ban, hoa
                    mơ, hoa đào… Thời tiết đẹp cũng khiến cho trời quang, các bạn có thể ngắm được trời, mây,
                    núi thật dễ dàng. Đây chính là một điểm hấp dẫn bậc nhất dành cho những ai muốn đi lên núi.
                    Đi trên đường ngắm những biển hoa, lên đỉnh ngắm những biển mây, bồng bềnh như trong tiên
                    cảnh, thật chẳng có gì hấp dẫn hơn.</p>
                <p><b><i>3, Chuẩn bị gì khi đi du lịch:</i></b> Cũng giống như bao chuyến du lịch khác, bạn cần
                    lưu ý chuẩn bị đồ đạc một cách chu đáo nhất nhưng cũng nhẹ nhàng nhất. Tới một vùng đất
                    nhiều điều lạ lẫm như các tỉnh miền núi chắc hẳn các bạn sẽ thấy thích và muốn mua nhiều
                    thứ. Để chừa vài chỗ trống trong va li, túi xách đôi khi rất hữu ích. Tuy nhiên các bạn cũng
                    nhớ, không nên có hiệu ứng đi du lịch, thấy gì cũng thích, thấy gì cũng mua, mua đồ lưu niệm
                    ở nơi du lịch thả ga nhé. Và mua thì nhớ mặc cả nhé. Người bán hàng dù là dân tộc nào thì
                    cũng biết nói thách hết đó.</p>`
    },
    {
        name: 'Kinh nghiệm đi du lịch miền Tây.',
        img: 'https://res.cloudinary.com/di4bpbe6z/image/upload/v1678457925/du_lich_mien_tay_rlh0qg.jpg',
        info: `<p><b> Được thiên nhiên ưu đãi cho yếu tố địa hình sông nước với những vườn trái cây trĩu quả,
                    những cánh đồng lúa thẳng cánh cò bay, vì thế nên miền Tây luôn là điểm đến lý tưởng để
                    du khách hòa mình vào thiên nhiên, sau những ngày làm việc bận rộn nơi phố thị ồn ào.</b></p>
                <p><b><i> 1, Thời gian lý tưởng đi du lịch miền Tây:</i></b> Thường vào mùa hè (khoảng tháng 6,
                    7, 8) là mùa trái cây chín ở miền Tây nên nếu bạn thích khám phá những vườn trái cây xanh
                    tươi thì nên đi vào mùa hè. Tầm tháng 9 đến tháng 11 là mùa nước nổi, đến miền Tây vào mùa
                    này bạn sẽ thấy nước ngập trắng cả đồng ruộng, đâu đâu cũng thấy nước. Du lịch miền Tây mùa
                    này tuy không được đi tham quan nhiều nơi nhưng nếu đến đúng vào những ngày nước nổi thì
                    cũng có nhiều thú vui không kém. Từ tháng 12 đến tháng 1, tháng 2 dương lịch là thời điểm
                    gần giáp tết. Đến miền Tây dịp này bạn có thể đi thăm các làng hoa nổi tiếng như Sa Đéc, Tân
                    Quy Đông, Vị Thanh…</p>
                <p><b><i>2, Mặc gì khi đi du lịch miền Tây:</i></b> Chỉ cần mang theo quần áo bình thường, áo
                    khoác để tránh nắng. Địa hình miền Tây nhiều sông nước nên tốt hơn hết bạn nên mang đồ có
                    vải màu, dễ giặt . Giày dép nên chọn những loại dễ đi, giày đế mềm, dép quai hậu. Đặc biệt
                    không nên đi giày cao gót vì đi ghe, thuyền và qua những cây cầu sẽ rất khó khăn. Mang theo
                    những loại thuốc chống côn trùng như: muỗi, rết,…. Vì khu vực sông nước thì thường rất nhiều
                    loại động vật này. Có thể chuẩn bị thêm đèn pin, gậy chống và võng để có thể đi lại và nghỉ
                    ngơi thoải mái hơn. Hạn chế đi lại vào ban đêm.</p>
                <p><b><i>3, Các món đặc sản miền Tây:</i></b></p>
                <p><b>+ Bún cá: </b>Đối với khu vực sông nước như Miên Tây thì bún cá là một món ăn khá phổ
                    biển, ở mỗi tỉnh thành khác nhau sẽ có những phương pháp chế biến khác nhau. Bạn có thể thử
                    mùi vị của bún cá Châu Đốc, bún cá Kiên Giang, bún cá Sóc Trăng….</p>
                <p><b>+ Cá lóc nướng trui.</b></p>
                <p><b>+ Cháo cá lóc: </b>Nhiều người biết đến đây là loài cá có độc, có thể gây ngộ độc nhưng
                    với những người dân ở đây thì việc chế biến nó đã trở thành quá quen thuộc. Những bát cháo
                    cá lóc bùi bùi, vị thơm, ngọt của cá lóc là những hương vị làm bạn sẽ nhớ mãi về vùng đất
                    miền Tây này.</p>
                <p><b>+ Lẩu mắm: </b>Lẩu mắm là món ăn đã có ở Cần Thơ từ rất lâu đời và được khen là món ăn
                    ngon nhất nhì ở miền Tây sông nước mà du khách không thể bỏ qua. Nguyên liệu chính được làm
                    từ mắm sặc hay mắm cá linh ở xứ Châu Đốc – An Giang, nước lẩu được nấu từ mắm với nước dừa
                    hoặc nước hầm xương heo. Bạn có thể thưởng thức thêm các loại lẩu khác như lẩu cua đồng, lẩu
                    cá linh bông điên điển…</p>`
            }
]