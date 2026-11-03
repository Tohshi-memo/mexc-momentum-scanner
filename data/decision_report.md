# Decision Report

- generated_at: 2026-11-03T06:01:26.653021+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18060**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=18060, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.36% | **+0.30%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.73% | **+0.25%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.19% | **+0.17%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.21% | **+0.11%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.16% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 260件 (TP 96 / SL 156 / EXP 8)
- 最新: EVAA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,521.09** / 初期 $100.00 (+1421.09%)
- 確定: 6912件 (Win 2000 / Loss 2216 / Flat 2696) / skip 7709件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,521.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.70** / 初期 $100.00 (+281.70%)
- 確定: 4486件 (Win 1204 / Loss 1000 / Flat 2282) / skip 6985件
- 成長率目線: 平均log +0.000299 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0505 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $381.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6221件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T06:01:13.465588+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=76600.0
- Funnel: target 1093 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +33.59% | $16,213,785.88 |
| ICNT/USDT:USDT | +17.19% | $1,307,274.97 |
| UAI/USDT:USDT | +15.52% | $6,622,455.89 |
| JCT/USDT:USDT | +13.43% | $2,574,338.98 |
| EVAA/USDT:USDT | +12.40% | $7,111,059.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +0.91% | +0.95% |
| LYN/USDT:USDT | below_1h_threshold | +0.75% | +0.79% |
| RUNE/USDT:USDT | below_1h_threshold | +0.73% | +0.77% |
| UAI/USDT:USDT | below_1h_threshold | +0.66% | +0.69% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.46% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
