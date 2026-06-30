# Decision Report

- generated_at: 2026-06-30T14:14:28.695413+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7905**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7905, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.42% | **-0.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.81% | **+0.38%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.35% | **+0.35%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.76% | **+0.19%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.41% | **+0.17%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.90% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.04% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2111件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.62** / 初期 $100.00 (+6.62%)
- 確定: 458件 (Win 121 / Loss 119 / Flat 218) / skip 858件
- 成長率目線: 平均log +0.000140 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0306 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.62

## 5. Latest Market Context

- 更新: 2026-06-30T14:14:22.416630+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=58977.7
- Funnel: target 818 → liquid 156 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1, 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +52.91% | $53,817,949.43 |
| IN/USDT:USDT | +45.80% | $1,678,660.77 |
| AIGENSYN/USDT:USDT | +36.11% | $14,460,979.70 |
| ANSEM/USDT:USDT | +34.91% | $1,108,822.79 |
| CAP/USDT:USDT | +29.87% | $5,109,298.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIVER/USDT:USDT | below_1h_threshold | +3.01% | +2.56% |
| H/USDT:USDT | below_1h_threshold | +2.67% | +2.21% |
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +2.50% | +2.05% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +2.49% | +2.04% |
| CAP/USDT:USDT | below_1h_threshold | +2.47% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
