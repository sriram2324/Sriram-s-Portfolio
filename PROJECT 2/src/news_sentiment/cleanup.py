"""Safe cleanup and session reset module.
Implements strictly scoped temporary directory purging and safe Streamlit state resets.
"""

from pathlib import Path
import shutil
from typing import Any, Dict, List, Optional, Union

from news_sentiment.config import PROJECT_ROOT, TEMP_DIR


def is_safe_subpath(target_path: Path, allowed_root: Path) -> bool:
    """Verifies that target_path is strictly an inner subpath of allowed_root (not root itself)."""
    try:
        resolved_target = target_path.resolve()
        resolved_root = allowed_root.resolve()
        if resolved_target == resolved_root:
            return False
        return resolved_target.is_relative_to(resolved_root)
    except Exception:
        return False


def clean_temp_directory(
    temp_dir: Optional[Union[str, Path]] = None,
    allowed_root: Optional[Union[str, Path]] = None
) -> Dict[str, Any]:
    """Safely cleans up temporary test or upload files.
    
    Guarantees:
        - Scoped strictly to designated temporary test directories under PROJECT_ROOT.
        - NEVER removes production datasets, trained models, source code, or reports.
        - Tolerates already-missing files safely.
    """
    target = Path(temp_dir) if temp_dir else TEMP_DIR
    root = Path(allowed_root) if allowed_root else PROJECT_ROOT

    # Ensure target is not identical to root and is an inner subpath
    if not is_safe_subpath(target, root):
        return {
            "success": False,
            "error": f"Refusing to delete path '{target}' - not an isolated inner subpath of '{root}'.",
            "cleaned_files": 0
        }

    # Safeguard against deleting critical project directories
    protected_names = {
        "src", "data", "models", "reports", "tests", "scripts", ".git",
        "project 2", PROJECT_ROOT.name.lower()
    }
    if target.name.lower() in protected_names or target.resolve() == PROJECT_ROOT.resolve():
        return {
            "success": False,
            "error": f"Path '{target}' is a protected directory and cannot be cleaned.",
            "cleaned_files": 0
        }

    # Extra defense-in-depth: must be designated temp or test dir
    name_lower = target.name.lower()
    if not (name_lower.startswith(".temp") or "test" in name_lower or "tmp" in name_lower or "sandbox" in name_lower):
        return {
            "success": False,
            "error": f"Path '{target}' is not a designated temporary directory.",
            "cleaned_files": 0
        }

    if not target.exists():
        return {
            "success": True,
            "message": f"Target path '{target}' does not exist (already clean).",
            "cleaned_files": 0
        }

    removed_count = 0
    try:
        if target.is_file():
            target.unlink(missing_ok=True)
            removed_count = 1
        elif target.is_dir():
            for item in target.iterdir():
                try:
                    if item.is_file() or item.is_symlink():
                        item.unlink(missing_ok=True)
                        removed_count += 1
                    elif item.is_dir():
                        shutil.rmtree(item, ignore_errors=True)
                        removed_count += 1
                except Exception:
                    pass
            # Try removing the empty temp dir itself
            try:
                target.rmdir()
            except Exception:
                pass

        return {
            "success": True,
            "cleaned_path": str(target),
            "cleaned_files": removed_count
        }
    except Exception as exc:
        return {
            "success": False,
            "error": f"Error while cleaning '{target}': {str(exc)}",
            "cleaned_files": removed_count
        }


def reset_streamlit_session(session_state_dict: Any) -> List[str]:
    """Safely resets interactive session state keys in Streamlit.
    
    Leaves persistent models, disk datasets, and configuration intact.
    Takes a snapshot of keys before clearing to prevent runtime dict modification errors.
    """
    keys_to_reset = [
        "single_text_input",
        "single_input_text",
        "single_prediction_result",
        "session_history",
        "uploaded_csv_data",
        "uploaded_csv_clean",
        "batch_predictions_df",
        "batch_results_df",
        "batch_text_column",
        "batch_text_col",
        "batch_filter_sentiment",
        "batch_search_query",
        "active_tab",
        "demo_test_summary",
        "audit_df",
        "training_in_progress",
        "training_message",
        "confirm_reset",
        "clear_confirmed",
    ]

    cleared_keys: List[str] = []
    existing_keys = list(session_state_dict.keys()) if hasattr(session_state_dict, "keys") else []

    for k in existing_keys:
        if k in keys_to_reset or k.startswith("temp_") or k.startswith("filter_"):
            try:
                del session_state_dict[k]
                cleared_keys.append(k)
            except KeyError:
                pass

    return cleared_keys
