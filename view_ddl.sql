CREATE VIEW vw_ir_remote_info AS
    SELECT DISTINCT dev.*,
                    data.type,
                    data.rawData
      FROM ir_remote_data data
           JOIN
           ir_remote_device dev ON data.data = dev.rc_button_data;
