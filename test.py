#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tokenizer

token = tokenizer.DongDu(2)
str = u"Theo thống kê của Trung tâm điều hành chương trình chống ngập nước TP HCM, cơn mưa lớn nhất năm vào chiều 15/9 đã gây ngập 66 điểm khắp địa bàn, nơi sâu nhất là 0,5 m. Mưa lớn gây ngập trên diện rộng đúng giờ tan tầm đã khiến giao thông Sài Gòn rối loạn. Hàng nghìn xe máy, ôtô xếp hàng dài chôn chân, nhà dân bị ngập sâu trong nước... Giải thích về nguyên nhân dẫn đến tình trạng ngập \"cả thành phố\", ông Đỗ Tấn Long - Trưởng phòng Quản lý hệ thống thoát nước Trung tâm điều hành chương trình chống ngập TP HCM - cho biết, do hệ thống cống ở nội đô được thiết kế để thoát nước với lượng mưa 86 mm kéo dài trong 3 giờ. Tuy nhiên, cơn mưa chiều tối qua có vũ lượng lên đến 142 mm, lại kéo dài nhiều giờ liền nên cống không thể thoát kịp"
print token.segment(str)
