from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if a list contains any duplicate elements.
    
    Args:
        nums: List of integers to check
        
    Returns:
        True if duplicates found, False otherwise
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def main():
    """Main entry point for interactive duplicate checker."""
    print("=" * 50)
    print("  Duplicate Checker")
    print("=" * 50)
    print("\nEnter integers separated by spaces")
    print("Example: 1 2 3 2 4")
    print()
    
    while True:
        try:
            user_input = input("Enter numbers: ").strip()
            
            if not user_input:
                print("⚠️  No input provided. Please try again.\n")
                continue
            
            # Parse input
            nums = list(map(int, user_input.split()))
            
            # Run the check
            has_duplicates = contains_duplicate(nums)
            
            # Display results
            print("\n" + "-" * 50)
            print(f"Input: {nums}")
            print(f"Result: {'✓ Duplicates found!' if has_duplicates else '✓ No duplicates'}")
            print("-" * 50 + "\n")
            
            # Ask if user wants to continue
            again = input("Check another list? (yes/no): ").strip().lower()
            if again not in ['yes', 'y']:
                print("\nThank you for using Duplicate Checker!")
                break
            print()
            
        except ValueError:
            print("❌ Invalid input! Please enter integers only.\n")


if __name__ == "__main__":
    main()