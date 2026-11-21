# Decision Report

- generated_at: 2026-11-21T14:26:22.519399+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19310**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19310, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.48% | **+1.24%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.27% | **+1.21%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.32% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.57% | **+2.28%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.88% | **+1.73%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +3.64% | **+1.64%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.92% | **+1.61%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +3.50% | **+1.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,675.95** / 初期 $100.00 (+1575.95%)
- 確定: 7453件 (Win 2138 / Loss 2400 / Flat 2915) / skip 8418件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $1,675.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$453.78** / 初期 $100.00 (+353.78%)
- 確定: 5115件 (Win 1362 / Loss 1095 / Flat 2658) / skip 7606件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0353 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $453.78

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7472件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000227 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T14:26:11.010810+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=60379.0
- Funnel: target 1086 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +54.97% | $1,192,088.69 |
| IDOL/USDT:USDT | +26.45% | $1,595,871.38 |
| RARE/USDT:USDT | +21.97% | $8,289,248.58 |
| VVV/USDT:USDT | +16.69% | $4,858,170.89 |
| PIEVERSE/USDT:USDT | +14.85% | $4,088,906.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +2.90% | +3.14% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.76% | +2.00% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.24% | +1.47% |
| BARD/USDT:USDT | below_1h_threshold | +0.86% | +1.10% |
| AKE/USDT:USDT | below_1h_threshold | +0.86% | +1.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
