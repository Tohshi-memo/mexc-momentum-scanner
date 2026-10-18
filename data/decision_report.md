# Decision Report

- generated_at: 2026-10-18T03:56:07.820506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16939**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.35% / filled 20/20。**
- 全期間 MARKET基準: n=16939, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.35% | **+2.35%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +4.22% | **+1.69%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.59% | **+1.35%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.35% | **+0.95%** |
| LIMIT_3PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.64% | **+0.45%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,284.52** / 初期 $100.00 (+1184.52%)
- 確定: 6405件 (Win 1865 / Loss 2050 / Flat 2490) / skip 7095件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DNA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $1,284.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.01** / 初期 $100.00 (+177.01%)
- 確定: 3704件 (Win 1031 / Loss 880 / Flat 1793) / skip 6646件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DNA/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $277.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5096件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-18T03:55:58.551873+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=81928.0
- Funnel: target 1084 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AVA/USDT:USDT | +17.12% | $2,323,718.61 |
| CLAUDIA/USDT:USDT | +15.78% | $2,318,597.07 |
| BR/USDT:USDT | +13.60% | $11,061,281.32 |
| Q/USDT:USDT | +11.00% | $8,813,497.34 |
| XMR/USDT:USDT | +10.84% | $6,752,279.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVA/USDT:USDT | below_1h_threshold | +3.14% | +2.97% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.77% | +1.60% |
| RAY/USDT:USDT | below_1h_threshold | +1.53% | +1.37% |
| USELESS/USDT:USDT | below_1h_threshold | +1.50% | +1.33% |
| ZRO/USDT:USDT | below_1h_threshold | +1.50% | +1.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
