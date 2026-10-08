# Decision Report

- generated_at: 2026-10-08T22:26:18.552262+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16378**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=16378, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/18 | 44.4% | +1.67% | **+0.74%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.81% | **+0.69%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.01% | **-0.00%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | -0.29% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.24** / 初期 $100.00 (+21.24%)
- 確定トレード: 236件 (TP 87 / SL 142 / EXP 7)
- 最新: STRK/USDT:USDT SL_HIT PnL -3.05% 残高後 $121.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,315.82** / 初期 $100.00 (+1215.82%)
- 確定: 6281件 (Win 1845 / Loss 2012 / Flat 2424) / skip 6658件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,315.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.04** / 初期 $100.00 (+174.04%)
- 確定: 3633件 (Win 1010 / Loss 853 / Flat 1770) / skip 6156件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0660 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PYTH/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $274.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4541件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000153 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-08T22:26:07.386448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=81751.4
- Funnel: target 1083 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +89.40% | $1,271,707.07 |
| BATON/USDT:USDT | +45.03% | $3,638,149.61 |
| OGN/USDT:USDT | +21.75% | $10,005,174.96 |
| SI/USDT:USDT | +19.50% | $1,677,532.61 |
| RLC/USDT:USDT | +17.80% | $18,860,965.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +4.47% | +4.36% |
| OGN/USDT:USDT | below_1h_threshold | +1.94% | +1.84% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.57% | +1.46% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.26% | +1.15% |
| IMX/USDT:USDT | below_1h_threshold | +1.10% | +0.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
