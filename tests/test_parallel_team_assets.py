from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent.parent


class ParallelTeamAssetsTests(unittest.TestCase):
    def test_command_declares_isolated_worktrees_and_no_automatic_integration(self):
        content = (ROOT / ".claude" / "commands" / "create_parallel_team.md").read_text(encoding="utf-8")

        self.assertIn("git worktree add -b agent/<alias>", content)
        self.assertIn("Ne pas pousser, fusionner, rebase ou déployer automatiquement.", content)
        self.assertIn("git status --short", content)

    def test_templates_require_branch_and_scope_boundaries(self):
        role = (ROOT / "templates" / "parallel_agents" / "agent_role_TEMPLATE.md").read_text(encoding="utf-8")
        team = (ROOT / "templates" / "parallel_agents" / "team_TEMPLATE.md").read_text(encoding="utf-8")

        self.assertIn("{{WORKTREE}}", role)
        self.assertIn("{{BRANCHE}}", role)
        self.assertIn("{{ECRITURE_AUTORISEE}}", role)
        self.assertIn("validation explicite de l'utilisateur", team)

    def test_communication_contract_preserves_direct_agents_and_messages(self):
        content = (ROOT / ".claude" / "commands" / "create_com_agents.md").read_text(encoding="utf-8")

        self.assertIn("messages.processing.md", content)
        self.assertIn("agents directs existants", content)


if __name__ == "__main__":
    unittest.main()
