# Decision Report

- generated_at: 2026-06-27T15:05:17.832633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7698**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7698, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +5.45% | **+0.82%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.43% | **+0.43%** |
| LIMIT_BB3S | 4/18 | 22.2% | +1.53% | **+0.34%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| ASK | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.90% | **+0.78%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.05% | **+0.53%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$232.52** / 初期 $100.00 (+132.52%)
- 確定: 2216件 (Win 662 / Loss 739 / Flat 815) / skip 2043件
- 成長率目線: 平均log +0.000381 / 幾何平均 +0.038% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $232.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.20** / 初期 $100.00 (+7.20%)
- 確定: 429件 (Win 116 / Loss 110 / Flat 203) / skip 680件
- 成長率目線: 平均log +0.000162 / 幾何平均 +0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0378 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGLD/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $107.20

## 5. Latest Market Context

- 更新: 2026-06-27T15:05:11.775590+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=60560.0
- Funnel: target 806 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +115.54% | $165,158,107.58 |
| MYX/USDT:USDT | +33.20% | $17,759,411.64 |
| SYRUP/USDT:USDT | +25.53% | $3,356,791.03 |
| SLX/USDT:USDT | +22.47% | $8,979,236.89 |
| PUNDIX/USDT:USDT | +18.90% | $6,611,948.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +3.62% | +3.67% |
| AGI/USDT:USDT | below_1h_threshold | +1.36% | +1.41% |
| BEAT/USDT:USDT | below_1h_threshold | +0.96% | +1.01% |
| BICO/USDT:USDT | below_1h_threshold | +0.91% | +0.96% |
| SLX/USDT:USDT | below_1h_threshold | +0.35% | +0.40% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
