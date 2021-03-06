from django.contrib import admin


class RunAdmin(admin.ModelAdmin):
    """
    GameAdmin allows admin to create or edit runs
    """

    list_display = ("id", "created_at", "name", "status")
    list_filter = ("created_at",)
    fieldsets = (
        (None, {"fields": (("id", "created_at", "name"), "status")}),
        (
            "Run parameters",
            {
                "fields": (
                    "data_board_len",
                    "inputs_version",
                    "max_search_threads_allowed",
                    "rating_game_probability",
                    "rating_game_high_elo_probability",
                    "rating_game_high_uncertainty_probability",
                    "rating_game_low_data_probability",
                    "rating_game_variability_scale",
                    "selfplay_startpos_probability",
                    "virtual_draw_strength",
                    "elo_number_of_iterations",
                    "selfplay_client_config",
                    "rating_client_config",
                    "git_revision_hash_whitelist",
                    "restrict_to_user_whitelist",
                    "user_whitelist",
                    "startpos_locked",
                    "startpos_total_weight",
                    "min_network_usage_delay",
                    "max_network_usage_delay",
                )
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        is_editing_existing_run = obj is not None
        if is_editing_existing_run:
            return (
                "id",
                "created_at",
                "name",
                "data_board_len",
                "inputs_version",
                "max_search_threads_allowed",
                "startpos_total_weight",
            )
        else:
            return "id", "created_at"
