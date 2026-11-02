# Decision Report

- generated_at: 2026-11-02T02:11:19.813003+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18005**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.13% / filled 20/20。**
- 全期間 MARKET基準: n=18005, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.31% | **+1.18%** |
| MARKET | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.25% | **+0.19%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.29% | **+0.13%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.02% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 258件 (TP 95 / SL 155 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,530.47** / 初期 $100.00 (+1430.47%)
- 確定: 6857件 (Win 1989 / Loss 2202 / Flat 2666) / skip 7709件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,530.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.35** / 初期 $100.00 (+281.35%)
- 確定: 4445件 (Win 1192 / Loss 986 / Flat 2267) / skip 6971件
- 成長率目線: 平均log +0.000301 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0901 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $381.35

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6163件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000256 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-02T02:11:08.839068+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78407.3
- Funnel: target 1088 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +30.06% | $13,101,250.01 |
| LYN/USDT:USDT | +21.90% | $1,538,538.18 |
| BEAMX/USDT:USDT | +14.27% | $4,430,111.01 |
| ESPORTS/USDT:USDT | +10.12% | $10,396,387.56 |
| Q/USDT:USDT | +9.04% | $5,419,279.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.09% | +4.03% |
| KORU/USDT:USDT | below_1h_threshold | +2.06% | +2.01% |
| Q/USDT:USDT | below_1h_threshold | +1.56% | +1.50% |
| EVAA/USDT:USDT | below_1h_threshold | +1.10% | +1.05% |
| NIULAI/USDT:USDT | below_1h_threshold | +0.87% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
