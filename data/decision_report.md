# Decision Report

- generated_at: 2026-07-17T23:11:13.222858+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8891**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=8891, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_BB3S | 3/19 | 15.8% | +5.04% | **+0.80%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +3.98% | **+0.40%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.70% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.35% | **+0.28%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.11% | **-0.08%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.28% | **-0.18%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$364.82** / 初期 $100.00 (+264.82%)
- 確定: 3006件 (Win 935 / Loss 955 / Flat 1116) / skip 2446件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $364.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.15** / 初期 $100.00 (+11.15%)
- 確定: 853件 (Win 201 / Loss 174 / Flat 478) / skip 1449件
- 成長率目線: 平均log +0.000124 / 幾何平均 +0.012% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0615 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $111.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.51** / 初期 $100.00 (-0.49%)
- 確定: 150件 (Win 48 / Loss 81 / Flat 21) / pending 3件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000195 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $99.51

## 6. Latest Market Context

- 更新: 2026-07-17T23:11:05.772747+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=63871.8
- Funnel: target 885 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +23.39% | $1,160,710.58 |
| ESPORTS/USDT:USDT | +18.78% | $9,170,548.59 |
| AKE/USDT:USDT | +13.12% | $48,674,650.74 |
| XEC/USDT:USDT | +7.62% | $3,345,755.44 |
| CRO/USDT:USDT | +6.59% | $2,074,335.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CASHCAT/USDT:USDT | below_1h_threshold | +4.67% | +4.80% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.16% | +1.28% |
| BULLA/USDT:USDT | below_1h_threshold | +0.74% | +0.87% |
| USOIL/USDT:USDT | below_1h_threshold | +0.67% | +0.80% |
| XEC/USDT:USDT | below_1h_threshold | +0.59% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
