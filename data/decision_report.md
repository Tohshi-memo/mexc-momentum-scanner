# Decision Report

- generated_at: 2026-11-20T01:36:28.289391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19228**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19228, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.45% | **-0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.40% | **+0.63%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.31% | **+0.65%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.37** / 初期 $100.00 (+1601.37%)
- 確定: 7386件 (Win 2122 / Loss 2378 / Flat 2886) / skip 8403件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HUMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,701.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.33** / 初期 $100.00 (+339.33%)
- 確定: 5052件 (Win 1348 / Loss 1087 / Flat 2617) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HUMA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $439.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7386件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T01:36:14.684650+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=62310.6
- Funnel: target 1084 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HUMA/USDT:USDT | +20.90% | $1,456,287.06 |
| RARE/USDT:USDT | +17.63% | $3,113,010.32 |
| SOXS/USDT:USDT | +16.20% | $49,551,284.97 |
| RAVE/USDT:USDT | +14.06% | $1,019,033.54 |
| UVXY/USDT:USDT | +12.86% | $2,976,843.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HUMA/USDT:USDT | below_1h_threshold | +4.79% | +4.48% |
| PIPPIN/USDT:USDT | below_1h_threshold | +4.47% | +4.16% |
| IRYS/USDT:USDT | below_1h_threshold | +3.96% | +3.65% |
| EVAA/USDT:USDT | below_1h_threshold | +3.69% | +3.38% |
| BTW/USDT:USDT | below_1h_threshold | +1.80% | +1.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
