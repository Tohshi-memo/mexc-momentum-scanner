# Decision Report

- generated_at: 2026-08-13T23:21:22.646980+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11491**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11491, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.81% | **+1.00%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.13% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.59% | **+1.03%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.86% | **+1.02%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.86% | **+0.84%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.18% | **+0.71%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3981件 (Win 1240 / Loss 1305 / Flat 1436) / skip 4071件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.35% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3252件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0164 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.27** / 初期 $100.00 (+16.27%)
- 確定: 1469件 (Win 433 / Loss 556 / Flat 480) / pending 1件 / skip 1494件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $116.27

## 6. Latest Market Context

- 更新: 2026-08-13T23:21:14.541504+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=63444.3
- Funnel: target 978 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +51.26% | $14,541,669.75 |
| US/USDT:USDT | +23.35% | $5,481,257.85 |
| WDAYSTOCK/USDT:USDT | +17.42% | $1,108,962.36 |
| PROM/USDT:USDT | +15.93% | $2,313,789.00 |
| H/USDT:USDT | +12.57% | $1,428,984.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +2.78% | +2.87% |
| SNXX/USDT:USDT | below_1h_threshold | +2.35% | +2.44% |
| AVNT/USDT:USDT | below_1h_threshold | +1.67% | +1.75% |
| AVAAI/USDT:USDT | below_1h_threshold | +1.51% | +1.60% |
| HOLO/USDT:USDT | below_1h_threshold | +1.36% | +1.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
