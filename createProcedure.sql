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
