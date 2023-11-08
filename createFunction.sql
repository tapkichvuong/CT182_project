SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER //
CREATE FUNCTION GetUserPassword(p_username VARCHAR(25))
RETURNS VARCHAR(64)
BEGIN
	DECLARE p_password VARCHAR(64);
	SELECT pass INTO p_password FROM taikhoan WHERE username = p_username;
    RETURN p_password;
END //
DELIMITER ;

