# Decision Report

- generated_at: 2026-11-11T05:46:20.325427+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18646**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=18646, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +2.47% | **+0.74%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.57% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_ATR | 4/20 | 20.0% | +1.51% | **+0.30%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.36% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.63% | **+0.98%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.28% | **+0.96%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +2.97% | **+0.89%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +1.94% | **+0.49%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 269件 (TP 97 / SL 164 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,657.69** / 初期 $100.00 (+1557.69%)
- 確定: 7210件 (Win 2073 / Loss 2305 / Flat 2832) / skip 7997件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,657.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4777件 (Win 1283 / Loss 1056 / Flat 2438) / skip 7280件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0101 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXL/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6805件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000558 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T05:46:09.603857+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=73778.1
- Funnel: target 1099 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +37.83% | $18,030,014.36 |
| MUU/USDT:USDT | +14.72% | $14,174,861.58 |
| FLOAT/USDT:USDT | +14.53% | $1,106,284.28 |
| CRWVSTOCK/USDT:USDT | +14.45% | $5,872,138.99 |
| KORU/USDT:USDT | +14.30% | $128,120,147.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JUP/USDT:USDT | below_1h_threshold | +1.08% | +0.98% |
| SNXX/USDT:USDT | below_1h_threshold | +0.80% | +0.70% |
| ICP/USDT:USDT | below_1h_threshold | +0.66% | +0.56% |
| ZKSYNC/USDT:USDT | below_1h_threshold | +0.66% | +0.56% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.46% | +0.36% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
