# Decision Report

- generated_at: 2026-07-01T16:11:14.622851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7999**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7999, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.83% | **-1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.47% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +6.03% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.67% | **+0.10%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.10% | **-0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.06% | **+1.44%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$270.75** / 初期 $100.00 (+170.75%)
- 確定: 2397件 (Win 731 / Loss 792 / Flat 874) / skip 2163件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $270.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.74** / 初期 $100.00 (+6.74%)
- 確定: 518件 (Win 131 / Loss 123 / Flat 264) / skip 892件
- 成長率目線: 平均log +0.000126 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0354 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.74

## 5. Latest Market Context

- 更新: 2026-07-01T16:11:08.601897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=60102.5
- Funnel: target 825 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| M/USDT:USDT | +6.44% | $7,435,571.70 |
| AIGENSYN/USDT:USDT | +2.59% | $6,238,556.90 |
| CAP/USDT:USDT | +2.00% | $4,826,159.21 |
| BEAT/USDT:USDT | +1.55% | $55,851,642.07 |
| SYN/USDT:USDT | +1.54% | $36,769,198.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.60% | +2.63% |
| CAP/USDT:USDT | below_1h_threshold | +2.09% | +2.11% |
| BEAT/USDT:USDT | below_1h_threshold | +1.56% | +1.59% |
| SYN/USDT:USDT | below_1h_threshold | +1.52% | +1.55% |
| CRV/USDT:USDT | below_1h_threshold | +1.34% | +1.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
