--FIRST

CREATE OR REPLACE FUNCTION return_filter(name_pattern VARCHAR)
  RETURNS TABLE(id INTEGER, name VARCHAR, phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY

    SELECT *
    FROM contacts
    WHERE contacts.name LIKE '%' || quote_ident(name_pattern) || '%';

END; $$

LANGUAGE plpgsql;

--SECOND
CREATE OR REPLACE PROCEDURE insert_user(v_name varchar, v_phone varchar)
AS
$$
BEGIN
    IF EXISTS (SELECT FROM contacts WHERE contacts.name = v_name) THEN
        UPDATE contacts SET phone = v_phone WHERE contacts.name = v_name;
    ELSE 
        INSERT INTO contacts (name, phone) VALUES(v_name, v_phone );
    END IF;
END; $$

LANGUAGE plpgsql;

--THIRD
CREATE OR REPLACE PROCEDURE add_users(VARIADIC v_vars varchar[])
AS
$$
BEGIN
    FOR i in 1..array_upper(v_vars, 1) by 2 LOOP
        IF v_vars[i+1] ~ '^(\+7|8)?\d{10}' THEN
            INSERT INTO contacts (name, phone) VALUES(v_vars[i], v_vars[i+1]);
        ELSE 
            RAISE NOTICE 'SORRY, THE NUMBER % IS INCORRECT', v_vars[i+1];
        END IF;
    END LOOP;
END;
$$
LANGUAGE plpgsql;

CALL add_users('ruslan', '87017604558', 'test123', '+77432346587', 'loh', '234313132');

--FOURTH
CREATE OR REPLACE FUNCTION pagination(page_size integer, page_number integer)
  RETURNS TABLE(id INTEGER, name VARCHAR, surname VARCHAR, phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY

    SELECT *
    FROM contacts
    LIMIT page_size OFFSET page_number*page_size;

END; $$

LANGUAGE plpgsql;

--FIFTH 
CREATE OR REPLACE PROCEDURE delete_user(v_opt varchar, v_var varchar)
AS
$$
BEGIN
    IF v_opt = 'name' THEN
        DELETE FROM contacts WHERE contacts.name = v_var;
    ELSIF v_opt = 'phone' THEN
        DELETE FROM contacts WHERE contacts.phone = v_var;
    END IF;
END; $$

LANGUAGE plpgsql;
----------------
CREATE OR REPLACE PROCEDURE delete_user_alt(v_var varchar)
AS
$$
BEGIN
    DELETE FROM contacts WHERE contacts.phone = v_var or contacts.name = v_var;
END; $$

LANGUAGE plpgsql;