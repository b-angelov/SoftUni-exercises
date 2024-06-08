-- Task 1

CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(30), last_name VARCHAR(30))
    RETURNS VARCHAR(60)
AS
    $$
        DECLARE
            full_name VARCHAR(60);
        BEGIN
            IF first_name IS NULL AND last_name IS NULL THEN
                full_name := NULL;
            ELSE
                full_name := TRIM(CONCAT(INITCAP(first_name),' ',INITCAP(last_name)));
            END IF;
            RETURN full_name;
        END;
    $$
LANGUAGE plpgsql;

-- select * from fn_full_name(NULL,'Gamgee');

-- Task 2

CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    initial_sum NUMERIC,
    yearly_interest_rate DECIMAL,
    number_of_years INT)
RETURNS NUMERIC
AS
    $$
        DECLARE
            result NUMERIC;
        BEGIN
            result := initial_sum * ((1 + yearly_interest_rate) ^ number_of_years);
            RETURN TRUNC(result,4);
        END;
    $$
LANGUAGE plpgsql;

-- select * from fn_calculate_future_value(500, 0.25, 10);

-- Task 3

CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    set_of_letters VARCHAR(50),
    word VARCHAR(50)
)
RETURNS BOOLEAN
AS
    $$
        BEGIN
            RETURN TRIM(LOWER(word), LOWER(set_of_letters)) = '';
        END;
    $$
LANGUAGE plpgsql;

-- select * from fn_is_word_comprised('R@o!B$B', 'Bob');

-- Task 4

CREATE OR REPLACE FUNCTION fn_is_game_over(
    is_game_over BOOLEAN
)
RETURNS TABLE (
    name VARCHAR(50),
    game_type_id INT,
    is_finished BOOLEAN
              )
AS
    $$
        BEGIN
            RETURN QUERY
            (
            SELECT
                g.name,
                g.game_type_id,
                g.is_finished
            FROM
                games as g
            WHERE
                g.is_finished = is_game_over
            );
        END;
    $$
LANGUAGE plpgsql;

-- select * from fn_is_game_over(false);

-- Task 5

CREATE OR REPLACE FUNCTION fn_difficulty_level(
    level INT
)
RETURNS VARCHAR(30)
AS
    $$
        DECLARE
            difficulty_level_verbose VARCHAR(30);
        BEGIN
            IF level <= 40 THEN
                difficulty_level_verbose := 'Normal Difficulty';
            ELSE IF level BETWEEN 41 AND 60 THEN
                difficulty_level_verbose := 'Nightmare Difficulty';
            ELSE
                difficulty_level_verbose := 'Hell Difficulty';
            END IF;
            END IF;
            RETURN difficulty_level_verbose;
        END;
    $$
LANGUAGE plpgsql;

SELECT
    user_id,
    level,
    cash,
    fn_difficulty_level(level) AS difficulty_level
FROM
    users_games
ORDER BY
    user_id;

-- Task 6

CREATE OR REPLACE FUNCTION fn_cash_in_users_games(
    game_name VARCHAR(50)
)
RETURNS TABLE (total_cash NUMERIC)
AS
$$
    BEGIN
        RETURN QUERY
        SELECT
            ROUND(cash, 2) AS total_cash
        FROM
            (SELECT
                game_id,
                cash,
                ROW_NUMBER() OVER (ORDER BY t.cash DESC) AS orders
            FROM
                (SELECT
                    *
                FROM
                    users_games AS ug
                JOIN
                    games AS g
                ON
                    ug.game_id = (SELECT id FROM games WHERE name = game_name)

                ) AS t
            GROUP BY
                game_id,
                cash) AS ot
        WHERE
            orders % 2 <> 0;
    END;
$$
LANGUAGE plpgsql;

-- SELECT * FROM fn_cash_in_users_games('Delphinium Pacific Giant');


-- Task 7

CREATE OR REPLACE PROCEDURE sp_retrieving_holders_with_balance_higher_than(
    searched_balance NUMERIC
)
AS
    $$
        DECLARE
            t RECORD;
        BEGIN
            FOR t IN
                SELECT
                     CONCAT(first_name, ' ', last_name) AS full_name,
                     SUM(balance) AS total_balance
                FROM
                    account_holders AS ah
                JOIN
                    accounts AS ac
                ON
                    ah.id = ac.account_holder_id
                GROUP BY
                    full_name
                HAVING
                    SUM(balance) > searched_balance
                ORDER BY
                    full_name
            LOOP
                RAISE NOTICE 'NOTICE: % - %', t.full_name,t.total_balance;
            END LOOP;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_retrieving_holders_with_balance_higher_than(200000);

-- Task 8

CREATE OR REPLACE PROCEDURE sp_deposit_money(
    account_id INT,
    money_amount NUMERIC(4)
)
AS
    $$
        BEGIN
            UPDATE
                accounts AS a
            SET
                balance = balance + money_amount
            WHERE
                a.id = account_id;
--             COMMIT;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_deposit_money(15,20000);

-- select * from accounts where id = 15;

-- Task 9

CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(4)
)
AS
    $$
        DECLARE
                current_balance NUMERIC(19,4);
        BEGIN

            UPDATE
                accounts AS a
            SET
                balance = balance - money_amount
            WHERE
                account_id = a.id;

            current_balance := ROUND((SELECT balance  FROM accounts  WHERE id = account_id ),4);

            IF
                current_balance < 0
            THEN
                RAISE NOTICE 'NOTICE: Insufficient balance to withdraw %', money_amount;
--                 ROLLBACK;
            ELSE
--                 COMMIT;
            END IF;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_withdraw_money(6, 5437.0000);
--
-- select * from accounts where id = 6;

-- Task 10

CREATE OR REPLACE PROCEDURE sp_transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC(19,4)
)
AS
    $$
        BEGIN
            CALL sp_withdraw_money(sender_id,amount);
            CALL sp_deposit_money(receiver_id, amount);

            IF (SELECT balance FROM accounts WHERE id = sender_id) < 0 THEN
                ROLLBACK;
            ELSE
                COMMIT;
            END IF;
        END;
    $$
LANGUAGE plpgsql;

-- CALL sp_transfer_money(13,15,400.9000);
--
-- select * from accounts where id in (13,15);

-- Task 11

DROP PROCEDURE sp_retrieving_holders_with_balance_higher_than;

-- Task 12

CREATE TABLE logs(
    id SERIAL PRIMARY KEY,
    account_id INT,
    old_sum NUMERIC(19,4),
    new_sum NUMERIC(19,4)
);

CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER
AS
    $$
        BEGIN
            INSERT INTO
                logs(
                     account_id,
                     old_sum,
                     new_sum
            )
            VALUES
            (OLD.id,OLD.balance,NEW.balance);
        RETURN NEW;
        END;
    $$
LANGUAGE plpgsql;

CREATE TRIGGER tr_account_balance_change
    AFTER UPDATE OF
        balance
    ON
        accounts
    FOR EACH ROW
    WHEN
        ( OLD.balance <> NEW.balance)
    EXECUTE FUNCTION
    trigger_fn_insert_new_entry_into_logs();

-- select * from accounts where id = 1;
--
-- UPDATE accounts
-- SET balance = 150.00
-- WHERE "id" = 1;
--
--
-- select * from logs;

-- Task 13

CREATE TABLE notification_emails(
    id SERIAL PRIMARY KEY,
    recipient_id INT,
    subject VARCHAR(200),
    body VARCHAR(500)
);

CREATE OR REPLACE FUNCTION trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER
AS
    $$
        BEGIN
           INSERT INTO
               notification_emails(
                    recipient_id,
                    subject,
                    body
               )
            VALUES(
                   OLD.id,
                   CONCAT('Balance change for account: ', NEW.id),
                   CONCAT('On ', NOW()::DATE,' your balance was changed from ',OLD.old_sum, ' to ',NEW.new_sum, '.')
                  );
           RETURN NEW;
        END;
    $$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER tr_send_email_on_balance_change
    AFTER UPDATE ON
        logs
    FOR EACH ROW
    EXECUTE FUNCTION
        trigger_fn_send_email_on_balance_change();

update logs set new_sum = new_sum + 100 where id = 1;

select * from notification_emails;
