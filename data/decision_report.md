# Decision Report

- generated_at: 2026-11-21T13:31:41.579905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19307**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19307, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +2.05% | **+1.03%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.36% | **+0.68%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.93% | **+5.93%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.41% | **+1.88%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.94% | **+1.74%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,667.70** / 初期 $100.00 (+1567.70%)
- 確定: 7450件 (Win 2137 / Loss 2399 / Flat 2914) / skip 8418件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,667.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$454.60** / 初期 $100.00 (+354.60%)
- 確定: 5112件 (Win 1361 / Loss 1093 / Flat 2658) / skip 7606件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0306 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $454.60

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7469件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000299 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T13:31:23.351541+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.17% price=59520.2
- Funnel: target 1086 → liquid 155 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +59.35% | $1,115,517.00 |
| IDOL/USDT:USDT | +32.47% | $1,165,815.45 |
| RARE/USDT:USDT | +21.97% | $7,747,314.81 |
| DODO/USDT:USDT | +20.78% | $1,216,046.15 |
| PIEVERSE/USDT:USDT | +14.97% | $3,949,796.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +4.56% | +3.39% |
| UNI/USDT:USDT | below_1h_threshold | +3.78% | +2.61% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.41% | +2.24% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +2.94% | +1.78% |
| VET/USDT:USDT | below_1h_threshold | +2.64% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
