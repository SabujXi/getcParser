def generate_error_message(text, text_rest):
    err_before_txt = '_' * (len(text) - len(text_rest))
    err_after_txt = '^' * len(text_rest)
    err_txt = '\n' + text + '\n' + err_before_txt + err_after_txt
    return err_txt
