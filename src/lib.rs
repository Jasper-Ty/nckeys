mod word;
mod shape;
mod matrix;

pub use word::*;

pub trait Degree {
    fn degree(&self) -> usize;
}

fn subsets(n: usize, k: usize) -> Vec<Vec<usize>> {
    let mut subsets = vec![]; 
    let mut stack = vec![vec![]];

    while let Some(partial_subset) = stack.pop() {
        if partial_subset.len() == k {
            subsets.push(partial_subset)
        } else {
            let i = partial_subset.last().map(|x| x+1).unwrap_or_default();
            for j in (i..n).rev() {
                let mut new_subset = partial_subset.clone();
                new_subset.push(j);
                stack.push(new_subset);
            }
        }
    }

    subsets
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn subsets_of_0() {
        let left = subsets(0,0);
        let right = vec![vec![]];
        assert_eq!(left, right);

        let left = subsets(0,1);
        let right: Vec<Vec<usize>> = vec![];
        assert_eq!(left, right);
    }

    #[test]
    fn subsets_of_1() {
        let left = subsets(1, 0);
        let right = vec![vec![]];
        assert_eq!(left, right);

        let left = subsets(1, 1);
        let right = vec![vec![0]];
        assert_eq!(left, right);

        let left = subsets(1, 2);
        let right: Vec<Vec<usize>> = vec![];
        assert_eq!(left, right);
    }

    #[test]
    fn subsets_of_2() {
        let left = subsets(2, 0);
        let right = vec![vec![]];
        assert_eq!(left, right);

        let left = subsets(2, 1);
        let right = vec![vec![0], vec![1]];
        assert_eq!(left, right);

        let left = subsets(2, 2);
        let right = vec![vec![0,1]];
        assert_eq!(left, right);

        let left = subsets(2, 3);
        let right: Vec<Vec<usize>> = vec![];
        assert_eq!(left, right);
    }

    #[test]
    fn subsets_of_3() {
        let left = subsets(3,0);
        let right = vec![vec![]];
        assert_eq!(left, right);

        let left = subsets(3,1);
        let right = vec![vec![0], vec![1], vec![2]];
        assert_eq!(left, right);

        let left = subsets(3,2);
        let right = vec![vec![0,1], vec![0,2], vec![1,2]];
        assert_eq!(left, right);

        let left = subsets(3,3);
        let right = vec![vec![0,1,2]];
        assert_eq!(left, right);

        let left = subsets(3, 4);
        let right: Vec<Vec<usize>> = vec![];
        assert_eq!(left, right);
    }

}