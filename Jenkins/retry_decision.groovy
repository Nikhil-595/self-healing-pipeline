class RetryDecision {
  static boolean shouldRetry(String analysis) {
    return analysis.toLowerCase().contains("retry") || analysis.toLowerCase().contains("clean workspace")
  }
}
return RetryDecision
