# Decision Report

- generated_at: 2026-10-28T03:16:46.217414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17671**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.73% / filled 20/20。**
- 全期間 MARKET基準: n=17671, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.73% | **+1.73%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.37% | **+1.23%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.82% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +4.00% | **+2.00%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.55% | **+1.28%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,532.91** / 初期 $100.00 (+1432.91%)
- 確定: 6760件 (Win 1968 / Loss 2170 / Flat 2622) / skip 7472件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,532.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$356.51** / 初期 $100.00 (+256.51%)
- 確定: 4200件 (Win 1144 / Loss 965 / Flat 2091) / skip 6882件
- 成長率目線: 平均log +0.000303 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1311 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $356.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5835件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000223 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T03:16:28.109566+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80921.7
- Funnel: target 1083 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +50.45% | $4,830,778.29 |
| SI/USDT:USDT | +42.27% | $1,232,804.87 |
| BULLA/USDT:USDT | +37.77% | $10,403,105.96 |
| APR/USDT:USDT | +15.86% | $6,235,206.68 |
| PONS/USDT:USDT | +14.86% | $2,130,018.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNITREE/USDT:USDT | below_1h_threshold | +3.57% | +3.56% |
| APR/USDT:USDT | below_1h_threshold | +3.10% | +3.10% |
| SI/USDT:USDT | below_1h_threshold | +2.29% | +2.28% |
| BEAT/USDT:USDT | below_1h_threshold | +2.12% | +2.12% |
| BANK/USDT:USDT | below_1h_threshold | +1.37% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
