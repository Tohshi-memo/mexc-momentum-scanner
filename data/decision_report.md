# Decision Report

- generated_at: 2026-10-08T15:01:31.906589+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16338**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.52% / filled 20/20。**
- 全期間 MARKET基準: n=16338, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +3.27% | **+0.98%** |
| LIMIT_4PCT | 10/20 | 50.0% | +1.20% | **+0.60%** |
| MARKET | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.42% | **+0.35%** |
| LIMIT_3PCT | 11/20 | 55.0% | +0.34% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.93% | **+0.47%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.23% | **+0.20%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.51% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6280件 (Win 1845 / Loss 2012 / Flat 2423) / skip 6619件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: OGN/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3632件 (Win 1010 / Loss 853 / Flat 1769) / skip 6117件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0126 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETHFI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4498件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T15:01:20.535001+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=82628.4
- Funnel: target 1082 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| OGN/USDT:USDT | +88.88% | $6,205,935.47 |
| MET/USDT:USDT | +31.73% | $34,078,314.90 |
| STRK/USDT:USDT | +24.58% | $9,773,266.20 |
| UAI/USDT:USDT | +17.08% | $3,388,716.69 |
| BOME/USDT:USDT | +13.62% | $1,566,034.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.82% | +0.86% |
| USOIL/USDT:USDT | below_1h_threshold | +0.68% | +0.72% |
| RLC/USDT:USDT | below_1h_threshold | +0.64% | +0.68% |
| OGN/USDT:USDT | below_1h_threshold | +0.54% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
