# Decision Report

- generated_at: 2026-07-17T22:46:12.502321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8889**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.54% / filled 20/20。**
- 全期間 MARKET基準: n=8889, expectancy=+0.01%
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
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_ATR | 8/20 | 40.0% | +1.29% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.35% | **+0.28%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | -0.05% | **-0.04%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | -0.28% | **-0.18%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | -0.50% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$112.93** / 初期 $100.00 (+12.93%)
- 確定トレード: 112件 (TP 43 / SL 65 / EXP 4)
- 最新: BSB/USDT:USDT TP_HIT PnL +8.00% 残高後 $112.93
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$362.05** / 初期 $100.00 (+262.05%)
- 確定: 3004件 (Win 934 / Loss 955 / Flat 1115) / skip 2446件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RESOLV/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $362.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.54** / 初期 $100.00 (+11.54%)
- 確定: 851件 (Win 201 / Loss 173 / Flat 477) / skip 1449件
- 成長率目線: 平均log +0.000128 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RESOLV/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $111.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.25** / 初期 $100.00 (-0.75%)
- 確定: 148件 (Win 47 / Loss 81 / Flat 20) / pending 3件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000204 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $99.25

## 6. Latest Market Context

- 更新: 2026-07-17T22:46:06.108199+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=63923.1
- Funnel: target 885 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +21.35% | $9,258,826.31 |
| AKE/USDT:USDT | +7.01% | $47,984,038.59 |
| VVV/USDT:USDT | +6.62% | $2,582,286.10 |
| XEC/USDT:USDT | +6.48% | $3,308,244.86 |
| CRO/USDT:USDT | +5.61% | $2,320,421.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.73% | +2.96% |
| UB/USDT:USDT | below_1h_threshold | +2.06% | +2.29% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.45% | +1.68% |
| USELESS/USDT:USDT | below_1h_threshold | +1.34% | +1.57% |
| SLX/USDT:USDT | below_1h_threshold | +1.01% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
