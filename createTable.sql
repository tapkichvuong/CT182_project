create table taikhoan(
	username varchar(25) primary key,
    pass varchar(64)
);


create table phuong(
	maphuong int primary key,
    tenphuong varchar(30),
    mahuyen int,
    CONSTRAINT FK_p_h FOREIGN KEY (mahuyen) REFERENCES huyen(mahuyen)
);

create table huyen(
	mahuyen int primary key,
    tenhuyen varchar(30)
);

create table docgia(
	madocgia varchar(8) primary key,
	firstname varchar(20),
    lastname varchar(20),
    gender int,
    birth date,
    phone varchar(10),
    email varchar(30),
	username varchar(25),
    maphuong int,
    diachi varchar(50),
    CONSTRAINT FK_dgtk FOREIGN KEY (username) REFERENCES taikhoan(username),
    CONSTRAINT FK_dgphuong FOREIGN KEY (maphuong) REFERENCES phuong(maphuong)
);

create table theloai(
	maloai int primary key AUTO_INCREMENT,
    tenloai varchar(20)
);

create table nxb(
	manxb int primary key AUTO_INCREMENT,
    tennxb varchar(30)
);

create table tacgia(
	matacgia int primary key AUTO_INCREMENT,
    tentacgia varchar(30)
);

create table sach(
	masach int primary key AUTO_INCREMENT,
    tensach varchar(50),
    matacgia int,
    manxb int,
    maloai int, 
    sl int,
    mota varchar(300),
    CONSTRAINT FK_sachnxb FOREIGN KEY (matacgia) REFERENCES tacgia(matacgia),
    CONSTRAINT FK_sachtheloai FOREIGN KEY (manxb) REFERENCES nxb(manxb),
    CONSTRAINT FK_sachtacgia FOREIGN KEY (maloai) REFERENCES theloai(maloai)
);

create table muon(
	masach int,
    madocgia varchar(8),
    ngaymuon date,
    ngaytra date null,
    matt int,
    CONSTRAINT FK_muonsach FOREIGN KEY (masach) REFERENCES sach(masach),
    CONSTRAINT FK_muontinhtrang FOREIGN KEY (matt) REFERENCES tinhtrang(matt),
    CONSTRAINT FK_muondocgia FOREIGN KEY (madocgia) REFERENCES docgia(madocgia)
);
create table tinhtrang(
	matt int primary key,
    tinhtrang varchar(20)
);



