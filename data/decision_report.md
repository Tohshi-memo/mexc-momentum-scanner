# Decision Report

- generated_at: 2026-11-18T19:01:24.127369+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19161**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19161, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.42% | **+0.19%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.33% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.63% | **+1.09%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.88% | **+0.57%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.40% | **+0.56%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,668.97** / 初期 $100.00 (+1568.97%)
- 確定: 7354件 (Win 2109 / Loss 2359 / Flat 2886) / skip 8368件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,668.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$430.70** / 初期 $100.00 (+330.70%)
- 確定: 5013件 (Win 1335 / Loss 1087 / Flat 2591) / skip 7559件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0358 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $430.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7324件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000147 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-18T19:01:13.236791+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.23% price=63003.2
- Funnel: target 1080 → liquid 143 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HUMA/USDT:USDT | +15.98% | $1,705,027.56 |
| PIPPIN/USDT:USDT | +15.18% | $5,120,475.35 |
| EVAA/USDT:USDT | +6.32% | $12,691,248.97 |
| BLESS/USDT:USDT | +6.28% | $20,798,667.21 |
| ARIA/USDT:USDT | +5.14% | $3,960,314.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLTRSTOCK/USDT:USDT | below_1h_threshold | +1.78% | +2.02% |
| KORU/USDT:USDT | below_1h_threshold | +1.13% | +1.36% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.29% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +1.28% |
| TQQQ/USDT:USDT | below_1h_threshold | +1.03% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
