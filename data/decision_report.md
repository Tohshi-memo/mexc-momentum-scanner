# Decision Report

- generated_at: 2026-10-22T22:21:30.686143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17173**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.52% / filled 20/20。**
- 全期間 MARKET基準: n=17173, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.52% | **+1.52%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.26% | **+1.13%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.05% | **+0.84%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.53% | **+0.32%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.37% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +1.36% | **+0.47%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,342.71** / 初期 $100.00 (+1242.71%)
- 確定: 6530件 (Win 1898 / Loss 2083 / Flat 2549) / skip 7204件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DNA/USDT:USDT `LIMIT_BB3S` SL_HIT account +0.05% 残高後 $1,342.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3850件 (Win 1055 / Loss 899 / Flat 1896) / skip 6734件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0291 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DNA/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5333件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000092 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T22:21:18.479645+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=81296.9
- Funnel: target 1096 → liquid 180 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +45.42% | $7,065,943.57 |
| DNA/USDT:USDT | +21.06% | $3,305,173.48 |
| AXIS/USDT:USDT | +4.35% | $1,874,748.16 |
| DASH/USDT:USDT | +4.33% | $14,315,066.77 |
| SOXS/USDT:USDT | +3.72% | $25,557,384.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +1.90% | +2.09% |
| AXIS/USDT:USDT | below_1h_threshold | +1.52% | +1.70% |
| CHIP/USDT:USDT | below_1h_threshold | +0.75% | +0.94% |
| EDGE/USDT:USDT | below_1h_threshold | +0.29% | +0.48% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.28% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
