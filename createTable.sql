create table taikhoan(
	username varchar(25) primary key,
    pass varchar(64)
);


create table phuong(
	maphuong int primary key,
    tenphuong varchar(30)
);

create table huyen(
	mahuyen int primary key,
    tenhuyen varchar(30)
);

create table docgia(
	madocgia varchar(8) primary key,
	fullname varchar(50),
    gender int,
    phone varchar(10),
    email varchar(30),
	username varchar(25),
    maphuong int,
    mahuyen int,
    CONSTRAINT FK_dgtk FOREIGN KEY (username) REFERENCES taikhoan(username),
    CONSTRAINT FK_dgphuong FOREIGN KEY (maphuong) REFERENCES phuong(maphuong),
    CONSTRAINT FK_dghuyen FOREIGN KEY (mahuyen) REFERENCES huyen(mahuyen)
);

create table theloai(
	maloai int primary key,
    tenloai varchar(20)
);

create table nxb(
	manxb int primary key,
    tennxb varchar(30)
);

create table tacgia(
	matacgia int primary key,
    tentacgia varchar(30)
);

create table sach(
	masach int primary key,
    tensach varchar(50),
    matacgia int,
    manxb int,
    maloai int, 
    mota varchar(300),
    CONSTRAINT FK_sachnxb FOREIGN KEY (matacgia) REFERENCES tacgia(matacgia),
    CONSTRAINT FK_sachtheloai FOREIGN KEY (manxb) REFERENCES nxb(manxb),
    CONSTRAINT FK_sachtacgia FOREIGN KEY (maloai) REFERENCES theloai(maloai)
);

create table muon(
	masach int,
    madocgia varchar(8),
    ngaymuon date,
    ngaytra date,
    trangthai int,
    CONSTRAINT FK_muonsach FOREIGN KEY (masach) REFERENCES sach(masach),
    CONSTRAINT FK_muondocgia FOREIGN KEY (madocgia) REFERENCES docgia(madocgia)
);

