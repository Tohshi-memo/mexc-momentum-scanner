# Decision Report

- generated_at: 2026-11-20T04:01:28.546256+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19229**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19229, expectancy=+0.02%
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
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.45% | **+0.65%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.31% | **+0.65%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.91% | **+0.45%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.24% | **+0.43%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.37** / 初期 $100.00 (+1601.37%)
- 確定: 7386件 (Win 2122 / Loss 2378 / Flat 2886) / skip 8404件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HUMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,701.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$439.33** / 初期 $100.00 (+339.33%)
- 確定: 5053件 (Win 1348 / Loss 1087 / Flat 2618) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0026 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: IRYS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $439.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7386件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T04:01:14.795237+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=62009.0
- Funnel: target 1084 → liquid 153 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOXS/USDT:USDT | +15.49% | $52,276,357.15 |
| HUMA/USDT:USDT | +14.58% | $1,471,490.15 |
| UVXY/USDT:USDT | +14.01% | $3,259,338.66 |
| RARE/USDT:USDT | +12.81% | $3,268,064.98 |
| BLESS/USDT:USDT | +11.72% | $8,950,601.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RARE/USDT:USDT | below_1h_threshold | +0.24% | +0.43% |
| NGAS/USDT:USDT | below_1h_threshold | +0.22% | +0.41% |
| EVAA/USDT:USDT | below_1h_threshold | +0.19% | +0.38% |
| MRNASTOCK/USDT:USDT | below_1h_threshold | +0.15% | +0.33% |
| BITO/USDT:USDT | below_1h_threshold | +0.12% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
