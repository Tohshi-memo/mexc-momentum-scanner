# Decision Report

- generated_at: 2026-08-13T09:46:23.724655+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11434**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=11434, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.49% | **+1.41%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.07% | **+1.03%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.72% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.52% | **+1.45%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.27% | **+1.27%** |
| LIMIT_FIB1272_LONG | 15/20 | 75.0% | +1.45% | **+1.09%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.05% | **+0.84%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$610.68** / 初期 $100.00 (+510.68%)
- 確定: 3952件 (Win 1234 / Loss 1292 / Flat 1426) / skip 4043件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $610.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.05** / 初期 $100.00 (+49.05%)
- 確定: 1622件 (Win 461 / Loss 385 / Flat 776) / skip 3223件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1349 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $149.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 1441件 (Win 423 / Loss 542 / Flat 476) / pending 2件 / skip 1460件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-13T09:46:15.485904+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=63679.8
- Funnel: target 973 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACU/USDT:USDT | +25.68% | $6,132,613.16 |
| BTW/USDT:USDT | +17.44% | $28,321,251.30 |
| APR/USDT:USDT | +12.11% | $15,456,465.45 |
| COTI/USDT:USDT | +11.83% | $10,109,665.44 |
| BANK/USDT:USDT | +11.19% | $4,836,361.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +1.94% | +2.04% |
| BTW/USDT:USDT | below_1h_threshold | +1.87% | +1.97% |
| ACU/USDT:USDT | below_1h_threshold | +1.48% | +1.58% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.14% | +1.24% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.00% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
