# Decision Report

- generated_at: 2026-06-01T09:12:23.128680+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5294**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5294, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.61% | **+0.88%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.03% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 961件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T09:12:20.656625+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=72986.9
- Funnel: target 775 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +159.03% | $34,145,092.68 |
| SLX/USDT:USDT | +130.06% | $5,660,989.77 |
| H/USDT:USDT | +84.71% | $27,574,066.96 |
| LAB/USDT:USDT | +54.12% | $203,442,230.26 |
| CTR/USDT:USDT | +18.34% | $1,668,266.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.60% | +4.45% |
| HOME/USDT:USDT | below_1h_threshold | +2.97% | +2.82% |
| BILL/USDT:USDT | below_1h_threshold | +2.96% | +2.81% |
| SLX/USDT:USDT | below_1h_threshold | +2.82% | +2.66% |
| H/USDT:USDT | below_1h_threshold | +2.40% | +2.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
