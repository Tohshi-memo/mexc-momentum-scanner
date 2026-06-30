# Decision Report

- generated_at: 2026-06-30T14:49:42.790388+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7911, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.47% | **-1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.83% | **+0.68%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.53% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.78% | **+0.57%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.69% | **+0.47%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.04% | **+2.04%** |
| ASK_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.76% | **+0.70%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +0.77% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2117件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.40** / 初期 $100.00 (+6.40%)
- 確定: 461件 (Win 122 / Loss 120 / Flat 219) / skip 861件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0280 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.40

## 5. Latest Market Context

- 更新: 2026-06-30T14:49:37.267761+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.20% price=58592.4
- Funnel: target 818 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.5 >= 65=1, 4h RSI 70.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IN/USDT:USDT | +70.02% | $4,116,605.23 |
| ANSEM/USDT:USDT | +40.83% | $1,156,367.23 |
| AIGENSYN/USDT:USDT | +36.11% | $14,657,294.69 |
| SYN/USDT:USDT | +33.68% | $57,441,589.55 |
| CAP/USDT:USDT | +26.16% | $5,502,484.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.23% | +3.44% |
| PYTH/USDT:USDT | below_1h_threshold | +3.02% | +3.22% |
| XLM/USDT:USDT | below_1h_threshold | +2.13% | +2.34% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.85% | +2.05% |
| UB/USDT:USDT | below_1h_threshold | +1.82% | +2.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
