#!/usr/bin/env python3
"""
Standup Story Generator - Because "still working on it" sounds suspicious
"""

import random
import sys

def generate_story():
    """Generate a plausible-sounding standup update with zero actual progress"""
    
    # Classic standup components
    yesterday_tasks = [
        "continued refactoring the authentication module",
        "investigated that intermittent bug in the API",
        "worked on optimizing database queries",
        "started implementing the new caching layer",
        "explored solutions for the race condition issue",
        "reviewed and updated documentation",
        "paired with a teammate on the deployment pipeline",
    ]
    
    blockers = [
        "waiting on a PR review",
        "blocked by a dependency update",
        "need clarification on requirements",
        "environment issues",
        "awaiting feedback from design",
        "investigating a weird test failure",
        "syncing with another team's changes",
    ]
    
    today_plans = [
        "continue with yesterday's work",
        "write more tests",
        "address the PR comments",
        "implement the feedback",
        "finish up the remaining tasks",
        "do some more research",
        "prepare for the demo",
    ]
    
    # The magic sauce: vague but technical-sounding phrases
    progress_phrases = [
        "making good progress",
        "almost there",
        "getting closer to completion",
        "working through the final details",
        "in the home stretch",
        "finalizing the implementation",
        "polishing up the solution",
    ]
    
    # Generate the masterpiece
    story = (
        f"Yesterday I {random.choice(yesterday_tasks)}. "
        f"I'm {random.choice(progress_phrases)}, "
        f"but currently {random.choice(blockers)}. "
        f"Today I'll {random.choice(today_plans)}."
    )
    
    return story

def main():
    """Print a fresh standup story to keep your team blissfully unaware"""
    print("\n📢 Your Standup Update:\n")
    print(generate_story())
    print("\n💡 Pro tip: Nod confidently while delivering this")

if __name__ == "__main__":
    main()