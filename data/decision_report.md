# Decision Report

- generated_at: 2026-06-27T23:16:56.542292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7717**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7717, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.76% | **-0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.61% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +0.73% | **+0.07%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |
| LIMIT_5PCT | 6/20 | 30.0% | -0.69% | **-0.21%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.72% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.76% | **+1.76%** |
| ASK_LONG | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.45% | **+0.94%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.74% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$237.17** / 初期 $100.00 (+137.17%)
- 確定: 2226件 (Win 668 / Loss 743 / Flat 815) / skip 2052件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $237.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.96** / 初期 $100.00 (+7.96%)
- 確定: 448件 (Win 120 / Loss 115 / Flat 213) / skip 680件
- 成長率目線: 平均log +0.000171 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0413 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $107.96

## 5. Latest Market Context

- 更新: 2026-06-27T23:16:51.572316+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=60023.7
- Funnel: target 806 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +11.38% | $2,377,300.14 |
| SLX/USDT:USDT | +9.47% | $18,802,484.03 |
| LAB/USDT:USDT | +7.77% | $42,147,389.08 |
| VELVET/USDT:USDT | +7.73% | $235,979,381.26 |
| HOT/USDT:USDT | +7.68% | $1,355,838.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAS/USDT:USDT | below_1h_threshold | +2.34% | +2.64% |
| BASED/USDT:USDT | below_1h_threshold | +1.99% | +2.29% |
| MYX/USDT:USDT | below_1h_threshold | +1.76% | +2.06% |
| ARX/USDT:USDT | below_1h_threshold | +1.74% | +2.04% |
| BEAT/USDT:USDT | below_1h_threshold | +1.41% | +1.71% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
