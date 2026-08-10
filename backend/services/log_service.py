"""
log_service.py

Service responsible for storing and retrieving
pipeline logs.
"""


import logging

from app.extensions import db
from app.models.log import Log

from sqlalchemy.exc import SQLAlchemyError



logger = logging.getLogger(__name__)




# ==========================================================
# Allowed levels
# ==========================================================

VALID_LEVELS = {

    "INFO",

    "WARNING",

    "ERROR"

}






# ==========================================================
# Add log
# ==========================================================

def add_log(

    analysis_id: int,

    message: str,

    level: str = "INFO"

):


    if level not in VALID_LEVELS:


        level = "INFO"




    try:



        log = Log(

            analysis_id=analysis_id,

            message=message,

            level=level

        )




        db.session.add(

            log

        )



        db.session.commit()



        return log





    except SQLAlchemyError as e:



        db.session.rollback()



        logger.error(

            f"[LOG_SERVICE_FAIL] "
            f"Impossible de sauvegarder le log "
            f"analyse={analysis_id}: {e}"

        )



        logger.warning(

            f"[LOST_LOG] [{level}] {message}"

        )



        return None





    except Exception as e:



        db.session.rollback()



        logger.error(

            f"[UNEXPECTED_LOG_ERROR] {e}"

        )



        return None







# ==========================================================
# Get logs by analysis
# ==========================================================

def get_logs_by_analysis(

    analysis_id: int

):


    return (

        db.session.query(Log)

        .filter_by(

            analysis_id=analysis_id

        )

        .order_by(

            Log.created_at.asc()

        )

        .all()

    )






# ==========================================================
# Delete logs
# ==========================================================

def delete_logs_by_analysis(

    analysis_id: int

):


    try:


        deleted = (

            db.session.query(Log)

            .filter_by(

                analysis_id=analysis_id

            )

            .delete()

        )



        db.session.commit()



        return deleted





    except SQLAlchemyError:



        db.session.rollback()



        return 0