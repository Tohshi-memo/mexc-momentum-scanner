# Decision Report

- generated_at: 2026-10-16T20:11:12.531791+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16825**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=16825, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.50% | **+1.50%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_BB3S | 6/13 | 46.2% | +1.45% | **+0.67%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.55% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.54% | **+0.85%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.21% | **+0.60%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.08% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.23% | **+0.49%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.15% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.60** / 初期 $100.00 (+21.60%)
- 確定トレード: 242件 (TP 90 / SL 145 / EXP 7)
- 最新: BTW/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,248.38** / 初期 $100.00 (+1148.38%)
- 確定: 6317件 (Win 1849 / Loss 2028 / Flat 2440) / skip 7069件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,248.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3688件 (Win 1027 / Loss 878 / Flat 1783) / skip 6548件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0730 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4984件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000383 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T20:11:03.078622+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=81629.2
- Funnel: target 1084 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +14.43% | $11,084,157.78 |
| UVXY/USDT:USDT | +10.34% | $2,562,262.60 |
| AKE/USDT:USDT | +6.93% | $10,593,640.88 |
| SOXS/USDT:USDT | +5.30% | $4,543,662.87 |
| ICNT/USDT:USDT | +4.19% | $2,765,018.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_relative_strength | +5.04% | +4.96% |
| AKE/USDT:USDT | below_1h_threshold | +2.94% | +2.86% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +2.58% | +2.50% |
| BTW/USDT:USDT | below_1h_threshold | +1.59% | +1.50% |
| SOXS/USDT:USDT | below_1h_threshold | +1.36% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
