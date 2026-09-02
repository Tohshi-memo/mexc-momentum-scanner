# Decision Report

- generated_at: 2026-09-02T13:31:18.156267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13335**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13335, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.27% | **+0.60%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.48% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.70% | **+1.08%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.06% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.20% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$831.77** / 初期 $100.00 (+731.77%)
- 確定: 4961件 (Win 1504 / Loss 1628 / Flat 1829) / skip 4935件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $831.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.36** / 初期 $100.00 (+74.36%)
- 確定: 2314件 (Win 643 / Loss 554 / Flat 1117) / skip 4432件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0359 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $174.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2711件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000187 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T13:31:10.438674+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=76814.4
- Funnel: target 1044 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +52.88% | $11,326,188.66 |
| MAGMA/USDT:USDT | +44.86% | $10,861,976.54 |
| FONE/USDT:USDT | +42.71% | $1,884,534.55 |
| UAI/USDT:USDT | +20.54% | $29,274,261.97 |
| CASHCAT/USDT:USDT | +18.48% | $1,943,164.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +1.62% | +1.30% |
| SILVER/USDT:USDT | below_1h_threshold | +1.31% | +0.99% |
| ARB/USDT:USDT | below_1h_threshold | +1.22% | +0.90% |
| SYRUP/USDT:USDT | below_1h_threshold | +1.19% | +0.87% |
| PYTH/USDT:USDT | below_1h_threshold | +1.15% | +0.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
