# Decision Report

- generated_at: 2026-05-15T05:45:04.531173+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4324**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.80% / filled 20/20。**
- 全期間 MARKET基準: n=4324, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=+2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.80% | **+2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.86% | **+2.86%** |
| MARKET | 20/20 | 100.0% | +2.80% | **+2.80%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.82% | **+2.25%** |
| LIMIT_2PCT | 14/20 | 70.0% | +3.10% | **+2.17%** |
| LIMIT_BB3S | 4/14 | 28.6% | +5.64% | **+1.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +1.24% | **+1.24%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.55% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.21** / 初期 $100.00 (-2.79%)
- 確定トレード: 44件 (TP 11 / SL 30 / EXP 3)
- 最新: SKYAI/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.42** / 初期 $100.00 (+20.42%)
- 確定: 376件 (Win 97 / Loss 131 / Flat 148) / skip 509件
- 成長率目線: 平均log +0.000494 / 幾何平均 +0.049% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $120.42

## 4. Latest Market Context

- 更新: 2026-05-15T05:45:01.159763+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=80444.1
- Funnel: target 765 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEAQ/USDT:USDT | +32.95% | $3,259,780.84 |
| GWEI/USDT:USDT | +23.31% | $1,152,451.30 |
| UP/USDT:USDT | +21.75% | $4,139,578.91 |
| FIGSTOCK/USDT:USDT | +12.00% | $3,156,470.04 |
| TAC/USDT:USDT | +10.47% | $2,132,422.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +1.90% | +2.20% |
| UP/USDT:USDT | below_1h_threshold | +1.12% | +1.41% |
| GWEI/USDT:USDT | below_1h_threshold | +0.86% | +1.16% |
| NAORIS/USDT:USDT | below_1h_threshold | +0.84% | +1.14% |
| USOIL/USDT:USDT | below_1h_threshold | +0.52% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
