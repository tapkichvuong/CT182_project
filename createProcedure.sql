DELIMITER //

CREATE PROCEDURE ChangePassword(
    IN p_madocgia VARCHAR(8),
    IN p_new_password VARCHAR(64)
)
BEGIN
    DECLARE user_exists INT;
    DECLARE p_username VARCHAR(25);
    -- Check if the user exists
    SELECT username INTO p_username
    FROM docgia
    WHERE madocgia = p_madocgia;
    SELECT COUNT(*) INTO user_exists
    FROM taikhoan
    WHERE username = p_username;
    
    -- If the user exists, change the password
    IF user_exists > 0 THEN
        UPDATE taikhoan SET pass = p_new_password WHERE username = p_username;
        SELECT 'Password changed successfully.' AS result;
    ELSE
        SELECT 'User does not exist.' AS result;
    END IF;
    
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE UpdateDocGia(
    IN p_madocgia VARCHAR(8),
    IN p_firstname VARCHAR(20),
    IN p_lastname VARCHAR(20),
    IN p_gender INT,
    IN p_birthdate DATE,
    IN p_phone VARCHAR(10),
    IN p_email VARCHAR(30),
    IN p_tenphuong VARCHAR(30),
    IN p_diachi VARCHAR(50)
)
BEGIN
    DECLARE p_maphuong INT;

    -- Get the maphuong corresponding to the provided tenphuong
    SELECT maphuong INTO p_maphuong FROM phuong WHERE tenphuong = p_tenphuong;

    -- Update docgia table
    UPDATE docgia
    SET 
        firstname = p_firstname,
        lastname = p_lastname,
        gender = p_gender,
        birth = p_birthdate,
        phone = p_phone,
        email = p_email,
        maphuong = p_maphuong,
        diachi = p_diachi
    WHERE
        madocgia = p_madocgia;
END //

DELIMITER ;

DELIMITER //
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_new_sach_muon`(
  IN madocgia_in varchar(8),
  IN masach_in INT,
  IN matt_in INT
)
BEGIN
IF NOT EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt =0
  ) THEN
    INSERT INTO muon (masach, madocgia, matt, ngaymuon)
    VALUES (masach_in, madocgia_in, matt_in, NOW());
    UPDATE sach SET sl = sl - 1
    WHERE masach = masach_in;
else
    select  'sach chua tra' as results;
  END IF;
END//
DELIMITER ;

DELIMITER $$
USE `qlthuvien`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_sach_muon`(
  IN madocgia_in varchar(8),
  IN masach_in INT,
  IN matt_in INT
)
BEGIN
IF EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt = 0 and date(now())-ngaymuon<=3
  ) THEN
    UPDATE muon SET matt=1, ngaytra=NOW() WHERE madocgia=madocgia_in and masach=masach_in and matt=0;
    
    UPDATE sach SET sl = sl + 1
    WHERE masach = masach_in;
elseif EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt = 0 and date(now())-ngaymuon>3
  ) THEN
    UPDATE muon SET matt=2, ngaytra=NOW() WHERE madocgia=madocgia_in and masach=masach_in and matt=0;
    UPDATE sach SET sl = sl + 1
    WHERE masach = masach_in;
else 
	select "a" as results; 
END IF;
END$$

DELIMITER ;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `tra_sach_mat_hong`(
  IN madocgia_in varchar(8),
  IN masach_in INT,
  IN matt_in INT
)
BEGIN
IF EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt = 0
  ) THEN
    UPDATE muon SET matt=matt_in WHERE madocgia=madocgia_in and masach=masach_in and matt=0;
elseif EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt = 3
  ) THEN
    UPDATE muon SET matt=5, ngaytra=NOW() WHERE madocgia=madocgia_in and masach=masach_in and matt=3;
    UPDATE sach SET sl = sl + 1
    WHERE masach = masach_in;
elseif EXISTS (
    SELECT * FROM muon WHERE madocgia = madocgia_in AND masach=masach_in and matt = 4
  ) THEN
    UPDATE muon SET matt=6, ngaytra=NOW() WHERE madocgia=madocgia_in and masach=masach_in and matt=4;
    UPDATE sach SET sl = sl + 1
    WHERE masach = masach_in;
else select('error ')as results;
  END IF;
END$$

CALL UpdateDocGia ('g8KL776S', 'admin', 'admin', 0, '2002-10-22', 'admin', 'admin@domain.com', 'Phường Châu Văn Liêm', '27 đường 26')
