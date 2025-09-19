import logging
import developer_config as cfg

def validate_resume(resume, role, jd_based):
    if not resume:
        logging.error("No resume provided")
        return "Resume file is required"
    if not resume.filename.endswith('.pdf'):
        logging.error("Invalid resume format: %s", resume.filename)
        return "Unsupported resume format. Only PDF format is allowed."
    logging.info("Resume validated successfully: %s", resume.filename)
    if not role:
        logging.error("Role is required for Resume analysis: No role provided")
        return "Role is required for Resume analysis"
    if role not in cfg.ROLE_REQUIREMENTS.keys():
        logging.error("Invalid role provided: %s", role)
        return f"Invalid role. Supported roles are: {', '.join(cfg.ROLE_REQUIREMENTS.keys())}"
    if type(jd_based) is not bool:
        logging.error("Invalid jd_based value: %s", jd_based)
        return "jd_based must be a boolean value"
    return None