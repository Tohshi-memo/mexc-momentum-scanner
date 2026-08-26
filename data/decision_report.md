# Decision Report

- generated_at: 2026-08-26T12:26:15.532374+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12705**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=12705, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/18 | 50.0% | +2.42% | **+1.21%** |
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.21% | **+0.97%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.14% | **+0.91%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.94% | **+0.90%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.73% | **+0.51%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.94% | **+0.47%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.65% | **+0.46%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.45% | **+0.16%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.33% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$696.98** / 初期 $100.00 (+596.98%)
- 確定: 4604件 (Win 1400 / Loss 1514 / Flat 1690) / skip 4662件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $696.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.06** / 初期 $100.00 (+57.06%)
- 確定: 2000件 (Win 544 / Loss 482 / Flat 974) / skip 4116件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0765 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $157.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.41** / 初期 $100.00 (+16.41%)
- 確定: 1977件 (Win 580 / Loss 754 / Flat 643) / pending 3件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.41

## 6. Latest Market Context

- 更新: 2026-08-26T12:26:06.187268+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=78600.1
- Funnel: target 1023 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +266.52% | $17,967,873.18 |
| BMT/USDT:USDT | +50.21% | $15,896,374.60 |
| TAC/USDT:USDT | +33.26% | $7,541,464.11 |
| LONGXIA/USDT:USDT | +33.07% | $1,992,942.10 |
| FARTCOIN/USDT:USDT | +18.96% | $21,179,106.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.48% | +3.28% |
| CYS/USDT:USDT | below_1h_threshold | +3.34% | +3.14% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.70% | +2.50% |
| EDEN/USDT:USDT | below_1h_threshold | +2.26% | +2.07% |
| USELESS/USDT:USDT | below_1h_threshold | +1.99% | +1.80% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
