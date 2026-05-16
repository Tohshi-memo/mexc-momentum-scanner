# Decision Report

- generated_at: 2026-05-16T00:08:22.799524+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4358**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4358, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.96% | **+0.29%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.64% | **+0.23%** |
| ASK | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.55% | **+0.22%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.67% | **+0.20%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.20** / 初期 $100.00 (-2.80%)
- 確定トレード: 47件 (TP 12 / SL 32 / EXP 3)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.20
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.99** / 初期 $100.00 (+17.99%)
- 確定: 390件 (Win 97 / Loss 136 / Flat 157) / skip 529件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_8PCT_LONG` SL_HIT account -0.50% 残高後 $117.99

## 4. Latest Market Context

- 更新: 2026-05-16T00:08:19.333081+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79146.8
- Funnel: target 759 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +26.16% | $3,275,165.34 |
| ARCSOL/USDT:USDT | +23.40% | $1,240,280.78 |
| LAB/USDT:USDT | +16.30% | $149,356,058.07 |
| STORJ/USDT:USDT | +16.30% | $4,786,060.83 |
| PEAQ/USDT:USDT | +13.03% | $5,016,980.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CGPT/USDT:USDT | below_1h_threshold | +2.13% | +2.04% |
| POLYX/USDT:USDT | below_1h_threshold | +1.86% | +1.77% |
| LAB/USDT:USDT | below_1h_threshold | +1.29% | +1.20% |
| TAC/USDT:USDT | below_1h_threshold | +1.10% | +1.01% |
| RAVE/USDT:USDT | below_1h_threshold | +0.80% | +0.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
