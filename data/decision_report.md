# Decision Report

- generated_at: 2026-06-01T10:02:24.544762+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5300**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5300, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.10% | **+0.41%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.26% | **+0.22%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.42% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 967件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T10:02:21.930801+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=72839.6
- Funnel: target 775 → liquid 126 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +135.19% | $35,258,391.96 |
| SLX/USDT:USDT | +97.26% | $6,592,001.89 |
| H/USDT:USDT | +87.78% | $29,396,158.42 |
| LAB/USDT:USDT | +69.37% | $206,292,590.34 |
| CTR/USDT:USDT | +18.23% | $1,708,702.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +2.81% | +2.82% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.37% | +2.38% |
| BILL/USDT:USDT | below_1h_threshold | +1.19% | +1.21% |
| ONDO/USDT:USDT | below_1h_threshold | +0.92% | +0.93% |
| MERL/USDT:USDT | below_1h_threshold | +0.67% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
