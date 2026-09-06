# Decision Report

- generated_at: 2026-09-06T14:01:11.326350+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13819**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.29% / filled 20/20。**
- 全期間 MARKET基準: n=13819, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.87% | **+1.41%** |
| LIMIT_3PCT | 12/20 | 60.0% | +2.02% | **+1.21%** |
| LIMIT_ATR | 11/20 | 55.0% | +1.59% | **+0.87%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.37% | **+0.83%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.10% | **+0.33%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +0.00% | **+0.00%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$845.62** / 初期 $100.00 (+745.62%)
- 確定: 5125件 (Win 1538 / Loss 1678 / Flat 1909) / skip 5255件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $845.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.51** / 初期 $100.00 (+91.51%)
- 確定: 2563件 (Win 717 / Loss 613 / Flat 1233) / skip 4667件
- 成長率目線: 平均log +0.000254 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0486 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $191.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.68** / 初期 $100.00 (+19.68%)
- 確定: 2430件 (Win 724 / Loss 926 / Flat 780) / pending 2件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000191 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $119.68

## 6. Latest Market Context

- 更新: 2026-09-06T14:01:02.073942+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=79777.3
- Funnel: target 1054 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAY/USDT:USDT | +63.64% | $7,897,733.57 |
| ARB/USDT:USDT | +45.12% | $180,425,819.71 |
| FONE/USDT:USDT | +43.35% | $1,081,630.82 |
| FLOCK/USDT:USDT | +28.99% | $2,376,335.27 |
| JUP/USDT:USDT | +20.66% | $9,636,220.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +0.24% | +0.26% |
| JUP/USDT:USDT | below_1h_threshold | +0.22% | +0.24% |
| 1000BONK/USDT:USDT | below_1h_threshold | +0.20% | +0.22% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.18% | +0.20% |
| FET/USDT:USDT | below_1h_threshold | +0.18% | +0.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
