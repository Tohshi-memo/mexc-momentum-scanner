# Decision Report

- generated_at: 2026-10-26T12:36:21.993491+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17481**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.24% / filled 20/20。**
- 全期間 MARKET基準: n=17481, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.51% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.11% | **+1.53%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +3.33% | **+1.16%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.86% | **+0.56%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6719件 (Win 1956 / Loss 2151 / Flat 2612) / skip 7323件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.14** / 初期 $100.00 (+219.14%)
- 確定: 4024件 (Win 1114 / Loss 951 / Flat 1959) / skip 6868件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0548 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5641件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T12:36:09.615179+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=80478.9
- Funnel: target 1073 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +58.61% | $4,256,877.55 |
| DOOD/USDT:USDT | +57.79% | $2,958,057.42 |
| BULLA/USDT:USDT | +56.37% | $3,600,795.26 |
| QNT/USDT:USDT | +18.49% | $93,358,180.94 |
| CHIP/USDT:USDT | +11.48% | $2,350,753.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +3.87% | +3.75% |
| SOXL/USDT:USDT | below_1h_threshold | +3.86% | +3.74% |
| MUU/USDT:USDT | below_1h_threshold | +2.66% | +2.54% |
| QNT/USDT:USDT | below_1h_threshold | +2.65% | +2.53% |
| SNXX/USDT:USDT | below_1h_threshold | +2.06% | +1.94% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
