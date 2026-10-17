# Decision Report

- generated_at: 2026-10-17T13:21:17.226548+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16877**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.28% / filled 20/20。**
- 全期間 MARKET基準: n=16877, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.28% | **+1.28%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.10% | **+0.99%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.03% | **+0.72%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.37% | **+0.68%** |
| LIMIT_3PCT | 10/20 | 50.0% | +1.11% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.76% | **+0.46%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.26% | **-0.17%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | -0.61% | **-0.22%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.94% | **-0.24%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | -0.26% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.35** / 初期 $100.00 (+1165.35%)
- 確定: 6351件 (Win 1855 / Loss 2033 / Flat 2463) / skip 7087件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $1,265.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3690件 (Win 1027 / Loss 878 / Flat 1785) / skip 6598件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5037件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000157 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T13:21:05.417093+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=81487.3
- Funnel: target 1084 → liquid 159 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +88.09% | $19,919,983.69 |
| Q/USDT:USDT | +33.47% | $1,305,617.07 |
| EPIC/USDT:USDT | +26.69% | $1,517,805.71 |
| BTW/USDT:USDT | +17.42% | $23,661,021.75 |
| ICNT/USDT:USDT | +16.41% | $9,365,562.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +4.18% | +4.18% |
| SIREN/USDT:USDT | below_1h_threshold | +2.72% | +2.72% |
| UVXY/USDT:USDT | below_1h_threshold | +1.24% | +1.24% |
| BTW/USDT:USDT | below_1h_threshold | +1.15% | +1.15% |
| LSK/USDT:USDT | below_1h_threshold | +0.28% | +0.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
